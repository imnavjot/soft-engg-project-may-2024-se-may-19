<template>
  <div class="container-fluid mt-5">
    <div class="row">
      <!-- Sidebar -->
      <SideBar
        :course="course"
        :activeWeek="activeWeek"
        @toggle-week="toggleWeek"
        @signout="signout"
        @go-to-dashboard="goToDashboard"
      />
      <!-- Right side: Course description and video player -->
      <main class="col-md-9 ml-sm-auto col-lg-9 px-md-4" style="position: relative; width: 80%; margin-left: auto;">
        <div v-if="selectedLecture">
          <!-- Show selected lecture details -->
          <h2 class="impressive-header">{{ selectedLecture.title }}</h2>
          <div class="embed-responsive embed-responsive-16by9">
            <div id="player"></div>
          </div>
          <AiSummary v-if="selectedLecture.id" :videoId="selectedLecture.id" :currentTime="currentVideoTime" />
          <IntegratedChatComponent />
        </div>
      </main>
      <QuestionPopup
        :showPopup="showPopup"
        :videoId="selectedLecture?.id"
        :currentTime="currentVideoTime"
        @close-popup="closePopup"
      />
    </div>
  </div>
</template>

<script>
/* global YT */
import SideBar from '../components/SideBar.vue';
import AiSummary from '../components/AiSummary.vue';
import QuestionPopup from '../components/QuestionPopup.vue';
import IntegratedChatComponent from '../components/IntegratedChatComponent.vue';


export default {
  name: 'CoursePage',
  components: {
    SideBar,
    AiSummary,
    QuestionPopup,
    IntegratedChatComponent
  },
  data() {
    return {
      course: null,
      selectedLecture: null,
      activeWeek: null,
      currentVideoTime: 0,
      player: null,
      showPopup: false,
      popupInterval: null,
      timeUpdateInterval: null,
    };
  },
  created() {
    this.initializeCourse();
  },
  methods: {
  async initializeCourse() {
    const courseId = this.$route.params.id;
    const lectureId = this.$route.params.lectureId;

    console.log('Initializing course with ID:', courseId, 'and lecture ID:', lectureId);

    try {
      const response = await fetch(`http://localhost:5000/course/${courseId}`);
      const data = await response.json();
      this.course = data;
      console.log('Fetched course data:', this.course);

      // Check if course data and weeks are available
      if (this.course && this.course.weeks) {
        for (const week of this.course.weeks) {
          const lecture = week.lectures.find(lec => lec.id.toString() === lectureId);
          if (lecture) {
            this.selectedLecture = lecture;
            console.log('Selected lecture:', this.selectedLecture);
            break;
          }
        }
        if (!this.selectedLecture) {
          console.error('Lecture not found for lectureId:', lectureId);
          this.$router.push(`/course/${this.course.id}`);
        } else {
          this.$nextTick(() => {
            this.initializePlayer();
          });
        }
      } else {
        console.error('Course data or weeks not found for courseId:', courseId);
      }
    } catch (error) {
      console.error('Error fetching course data for courseId:', courseId, 'Error:', error);
      // Handle error (e.g., show error message, redirect to error page)
    }
  },
    toggleWeek(weekId) {
      this.activeWeek = this.activeWeek === weekId ? null : weekId;
    },
    async signout() {
      try {
        const response = await fetch('http://localhost:5000/signout', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (response.ok) {
          this.$router.push('/login');
        } else {
          console.error('Error during signout:', response.statusText);
          // Handle error (e.g., show error message)
        }
      } catch (error) {
        console.error('Error during signout:', error);
        // Handle error (e.g., show error message)
      }
    },
    goToDashboard() {
      this.$router.push('/dashboard');
    },
    initializePlayer() {
      if (this.player) {
        this.player.destroy();
      }

      window.onYouTubeIframeAPIReady = () => {
        this.player = new YT.Player('player', {
          videoId: this.selectedLecture.videoUrl,
          playerVars: {
            'playsinline': 1
          },
          events: {
            'onReady': this.onPlayerReady,
            'onStateChange': this.onPlayerStateChange
          }
        });
      };

      if (!window.YT) {
        const tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        const firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
      } else {
        this.player = new YT.Player('player', {
          videoId: this.selectedLecture.video_url,
          playerVars: {
            'playsinline': 1
          },
          events: {
            'onReady': this.onPlayerReady,
            'onStateChange': this.onPlayerStateChange
          }
        });
      }
    },
    onPlayerReady() {
       console.log('YouTube player is ready');
       this.updateCurrentTime();
       this.startQuestionPopupTimer(); // Start the popup timer when player is ready
     },
     onPlayerStateChange(event) {
       console.log('Player state changed:', event.data);

       if (event.data === YT.PlayerState.PLAYING) {
         this.updateCurrentTime();
         this.startQuestionPopupTimer(); // Restart the timer if video is playing
         this.startTimeUpdateInterval();
       } else {
         this.clearQuestionPopupTimer(); // Stop the timer if video is paused or stopped
         this.clearTimeUpdateInterval();
       }
     },
     updateCurrentTime() {
       if (this.player && this.player.getCurrentTime) {
         this.currentVideoTime = this.player.getCurrentTime();
         console.log("Current video time in CoursePage.vue:", this.currentVideoTime);
       }
     },
     startTimeUpdateInterval() {
       // If an interval is already running, do nothing
       if (this.timeUpdateInterval) return;

       this.timeUpdateInterval = setInterval(() => {
         this.updateCurrentTime();
       }, 1000); // Update every 1 second
     },
     clearTimeUpdateInterval() {
       if (this.timeUpdateInterval) {
         clearInterval(this.timeUpdateInterval);
         this.timeUpdateInterval = null; // Clear the interval ID
       }
     },
     startQuestionPopupTimer() {
       // Clear any existing interval to prevent multiple intervals running simultaneously
       if (this.popupInterval) {
         clearInterval(this.popupInterval);
       }

       // Set up the interval to show the popup every 30 seconds
       this.popupInterval = setInterval(() => {
         if (this.player && this.player.getPlayerState() === YT.PlayerState.PLAYING) {
           this.showQuestionPopup();
         }
       }, 30000); // 30 seconds in milliseconds
     },
     clearQuestionPopupTimer() {
       if (this.popupInterval) {
         clearInterval(this.popupInterval);
         this.popupInterval = null;
       }
     },
     showQuestionPopup() {
       if (this.player) {
        this.player.pauseVideo(); // Pause the video when the popup is shown
        }
       this.showPopup = true;
     },
     closePopup() {
       this.showPopup = false;
       this.startQuestionPopupTimer(); // Restart the timer after the popup is closed
     }
   },

  watch: {
    '$route.params.lectureId'(newLectureId) {
      console.log('New lectureId:', newLectureId); // Check the new lectureId value

      if (newLectureId) {
        this.initializeCourse();
      }
    }
  },
  beforeUnmount() {
    this.clearQuestionPopupTimer(); // Clean up the interval when component is destroyed
  }
};
</script>

<style scoped>
.impressive-header {
  display: inline-block;
  font-size: 1.1em;
  font-weight: bold;
  color: #2c3e50;
  padding: 10px 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px 0;
  border-left: 5px solid #007bff;
  text-align: left;
}

.embed-responsive {
  position: relative;
  display: block;
  width: 100%;
  padding: 0;
  overflow: hidden;
}

.embed-responsive .embed-responsive-item {
  position: relative;
  top: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}
</style>
