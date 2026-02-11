---
title: AI-Enhanced Educational Platform API v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="ai-enhanced-educational-platform-api">AI-Enhanced Educational Platform API v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1>Software Engineering Project: Milestone 4</h1>
<h2>Task: API Endpoints Documentation</h2>
<h3>Course: BSCSS3001 - Software Engineering</h3>
<h3>Team  19 </h3>
<h3>Members:
<ul><li>NAVJOT	21f2000931@ds.study.iitm.ac.in</li>
<li>PRIYADARSHINI S	21f1001572@ds.study.iitm.ac.in</li>
<li>JAY KASHYAP	21f1002984@ds.study.iitm.ac.in</li>
<li>Aloney Neeraj	21f1006471@ds.study.iitm.ac.in</li>
<li>AMAL ROY	21f1004594@ds.study.iitm.ac.in)</li>
<li>BALASURYA K	22f3002744@ds.study.iitm.ac.in</li>
<li>SHELLEY R	21f1005512@ds.study.iitm.ac.in</li>
<li>AMAY S RANA	21f3002432@ds.study.iitm.ac.in</li>
</ul>
</h3>
<h3>Program: BS in Data Science and Applications</h3>
<h3>Institute: Indian Institute of Technology, Madras</h3>
</br></br>

<h1 id="ai-enhanced-educational-platform-api-default">Default</h1>

## post__content_summary

> Code samples

```shell
# You can also use wget
curl -X POST /content_summary \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /content_summary HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "videoId": "string",
  "type": "complete",
  "endTime": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/content_summary',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/content_summary',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/content_summary', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/content_summary', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/content_summary");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/content_summary", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /content_summary`

*Generate a summary for a video content*

> Body parameter

```json
{
  "videoId": "string",
  "type": "complete",
  "endTime": 0
}
```

<h3 id="post__content_summary-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» videoId|body|string|false|ID of the video|
|» type|body|string|false|Type of summary|
|» endTime|body|integer|false|End time for partial summary|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» type|complete|
|» type|partial|

> Example responses

> 200 Response

```json
{
  "summary": "string"
}
```

<h3 id="post__content_summary-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Summary generated successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__content_summary-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» summary|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__generate_questions

> Code samples

```shell
# You can also use wget
curl -X POST /generate_questions \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /generate_questions HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "videoId": "string",
  "endTime": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/generate_questions',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/generate_questions',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/generate_questions', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/generate_questions', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/generate_questions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/generate_questions", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /generate_questions`

*Generate multiple choice questions from video content*

> Body parameter

```json
{
  "videoId": "string",
  "endTime": 0
}
```

<h3 id="post__generate_questions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» videoId|body|string|false|ID of the video|
|» endTime|body|integer|false|End time for partial text extraction|

> Example responses

> 200 Response

```json
{
  "questions": [
    {
      "question": "string",
      "options": [
        "string"
      ],
      "correct": "string"
    }
  ]
}
```

<h3 id="post__generate_questions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Questions generated successfully|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__generate_questions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» questions|[object]|false|none|none|
|»» question|string|false|none|none|
|»» options|[string]|false|none|none|
|»» correct|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__evaluate_answers

> Code samples

```shell
# You can also use wget
curl -X POST /evaluate_answers \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /evaluate_answers HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "questions": [
    {
      "question": "string",
      "correct": "string"
    }
  ],
  "answers": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/evaluate_answers',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/evaluate_answers',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/evaluate_answers', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/evaluate_answers', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/evaluate_answers");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/evaluate_answers", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /evaluate_answers`

*Evaluate user answers*

> Body parameter

```json
{
  "questions": [
    {
      "question": "string",
      "correct": "string"
    }
  ],
  "answers": [
    "string"
  ]
}
```

<h3 id="post__evaluate_answers-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» questions|body|[object]|false|none|
|»» question|body|string|false|none|
|»» correct|body|string|false|none|
|» answers|body|[string]|false|none|

> Example responses

> 200 Response

```json
{
  "correct_count": 0
}
```

<h3 id="post__evaluate_answers-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Answers evaluated successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|

<h3 id="post__evaluate_answers-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» correct_count|integer|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__pdf_summary

> Code samples

```shell
# You can also use wget
curl -X POST /pdf_summary \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /pdf_summary HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "pdfUrl": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/pdf_summary',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/pdf_summary',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/pdf_summary', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/pdf_summary', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/pdf_summary");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/pdf_summary", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /pdf_summary`

*Generate a summary for a PDF document*

> Body parameter

```json
{
  "pdfUrl": "string"
}
```

<h3 id="post__pdf_summary-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» pdfUrl|body|string|false|URL of the PDF document|

> Example responses

> 200 Response

```json
{
  "summary": "string"
}
```

<h3 id="post__pdf_summary-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Summary generated successfully|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__pdf_summary-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» summary|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__ppa_test_run

> Code samples

```shell
# You can also use wget
curl -X POST /ppa_test_run \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /ppa_test_run HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "code": "string",
  "testCases": [
    {
      "input": [
        "string"
      ],
      "expected": "string"
    }
  ],
  "functionName": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/ppa_test_run',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/ppa_test_run',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/ppa_test_run', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/ppa_test_run', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/ppa_test_run");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/ppa_test_run", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /ppa_test_run`

*Run public tests for provided code*

> Body parameter

```json
{
  "code": "string",
  "testCases": [
    {
      "input": [
        "string"
      ],
      "expected": "string"
    }
  ],
  "functionName": "string"
}
```

<h3 id="post__ppa_test_run-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» code|body|string|false|none|
|» testCases|body|[object]|false|none|
|»» input|body|[string]|false|none|
|»» expected|body|string|false|none|
|» functionName|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "results": {
    "public": [
      {
        "input": [
          "string"
        ],
        "expected": "string",
        "output": "string",
        "result": "string"
      }
    ]
  }
}
```

<h3 id="post__ppa_test_run-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Test results|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__ppa_test_run-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» results|object|false|none|none|
|»» public|[object]|false|none|none|
|»»» input|[string]|false|none|none|
|»»» expected|string|false|none|none|
|»»» output|string|false|none|none|
|»»» result|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__ppa_submit

> Code samples

```shell
# You can also use wget
curl -X POST /ppa_submit \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /ppa_submit HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "code": "string",
  "testCases": [
    {
      "input": [
        "string"
      ],
      "expected": "string"
    }
  ],
  "functionName": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/ppa_submit',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/ppa_submit',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/ppa_submit', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/ppa_submit', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/ppa_submit");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/ppa_submit", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /ppa_submit`

*Submit code and run all tests*

> Body parameter

```json
{
  "code": "string",
  "testCases": [
    {
      "input": [
        "string"
      ],
      "expected": "string"
    }
  ],
  "functionName": "string"
}
```

<h3 id="post__ppa_submit-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» code|body|string|false|none|
|» testCases|body|[object]|false|none|
|»» input|body|[string]|false|none|
|»» expected|body|string|false|none|
|» functionName|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "results": {
    "public": [
      {
        "input": [
          "string"
        ],
        "expected": "string",
        "output": "string",
        "result": "string"
      }
    ],
    "private": [
      {
        "input": [
          "string"
        ],
        "expected": "string",
        "output": "string",
        "result": "string"
      }
    ]
  }
}
```

<h3 id="post__ppa_submit-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Test results|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__ppa_submit-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» results|object|false|none|none|
|»» public|[object]|false|none|none|
|»»» input|[string]|false|none|none|
|»»» expected|string|false|none|none|
|»»» output|string|false|none|none|
|»»» result|string|false|none|none|
|»» private|[object]|false|none|none|
|»»» input|[string]|false|none|none|
|»»» expected|string|false|none|none|
|»»» output|string|false|none|none|
|»»» result|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__pseudocode

> Code samples

```shell
# You can also use wget
curl -X POST /pseudocode \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /pseudocode HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "question": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/pseudocode',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/pseudocode',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/pseudocode', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/pseudocode', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/pseudocode");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/pseudocode", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /pseudocode`

*Generate pseudocode for a problem statement*

> Body parameter

```json
{
  "question": "string"
}
```

<h3 id="post__pseudocode-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» question|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "pseudocode": "string"
}
```

<h3 id="post__pseudocode-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Pseudocode generated successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__pseudocode-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» pseudocode|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__analyze

> Code samples

```shell
# You can also use wget
curl -X POST /analyze \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /analyze HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "code": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/analyze',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/analyze',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/analyze', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/analyze', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/analyze");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/analyze", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /analyze`

*Analyze code for quality issues*

> Body parameter

```json
{
  "code": "string"
}
```

<h3 id="post__analyze-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» code|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "issues": "string"
}
```

<h3 id="post__analyze-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Code analysis|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__analyze-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» issues|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__feedback

> Code samples

```shell
# You can also use wget
curl -X POST /feedback \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /feedback HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "code": "string",
  "results": [
    {
      "input": [
        "string"
      ],
      "expected": "string",
      "output": "string",
      "result": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/feedback',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/feedback',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/feedback', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/feedback', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/feedback");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/feedback", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /feedback`

*Provide feedback for code errors*

> Body parameter

```json
{
  "code": "string",
  "results": [
    {
      "input": [
        "string"
      ],
      "expected": "string",
      "output": "string",
      "result": "string"
    }
  ]
}
```

<h3 id="post__feedback-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» code|body|string|false|none|
|» results|body|[object]|false|none|
|»» input|body|[string]|false|none|
|»» expected|body|string|false|none|
|»» output|body|string|false|none|
|»» result|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "feedback": "string"
}
```

<h3 id="post__feedback-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Feedback generated successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__feedback-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» feedback|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__improvement

> Code samples

```shell
# You can also use wget
curl -X POST /improvement \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /improvement HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "code": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/improvement',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/improvement',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/improvement', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/improvement', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/improvement");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/improvement", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /improvement`

*Suggest code improvements*

> Body parameter

```json
{
  "code": "string"
}
```

<h3 id="post__improvement-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» code|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "improvements": "string"
}
```

<h3 id="post__improvement-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Improvement suggestions|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__improvement-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» improvements|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__gaanswers

> Code samples

```shell
# You can also use wget
curl -X POST /gaanswers \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /gaanswers HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "answers": [
    {
      "question_id": "string",
      "selected": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/gaanswers',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/gaanswers',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/gaanswers', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/gaanswers', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/gaanswers");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/gaanswers", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /gaanswers`

*Evaluate general assignment answers*

> Body parameter

```json
{
  "answers": [
    {
      "question_id": "string",
      "selected": "string"
    }
  ]
}
```

<h3 id="post__gaanswers-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» answers|body|[object]|false|none|
|»» question_id|body|string|false|none|
|»» selected|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "correct_count": 0,
  "feedback": [
    {
      "question": "string",
      "correct_answer": "string",
      "selected_answer": "string"
    }
  ]
}
```

<h3 id="post__gaanswers-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Evaluation results|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__gaanswers-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» correct_count|integer|false|none|none|
|» feedback|[object]|false|none|none|
|»» question|string|false|none|none|
|»» correct_answer|string|false|none|none|
|»» selected_answer|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__gaimprovement

> Code samples

```shell
# You can also use wget
curl -X POST /gaimprovement \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /gaimprovement HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "feedback": [
    {
      "question": "string",
      "correct_answer": "string",
      "selected_answer": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/gaimprovement',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/gaimprovement',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/gaimprovement', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/gaimprovement', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/gaimprovement");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/gaimprovement", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /gaimprovement`

*Provide suggestions for general assignment improvements*

> Body parameter

```json
{
  "feedback": [
    {
      "question": "string",
      "correct_answer": "string",
      "selected_answer": "string"
    }
  ]
}
```

<h3 id="post__gaimprovement-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» feedback|body|[object]|false|none|
|»» question|body|string|false|none|
|»» correct_answer|body|string|false|none|
|»» selected_answer|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "improvements": "string"
}
```

<h3 id="post__gaimprovement-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Improvement suggestions|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__gaimprovement-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» improvements|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__paanswers

> Code samples

```shell
# You can also use wget
curl -X POST /paanswers \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /paanswers HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "answers": [
    {
      "question_id": "string",
      "selected": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/paanswers',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/paanswers',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/paanswers', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/paanswers', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/paanswers");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/paanswers", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /paanswers`

*Evaluate practice assignment answers*

> Body parameter

```json
{
  "answers": [
    {
      "question_id": "string",
      "selected": "string"
    }
  ]
}
```

<h3 id="post__paanswers-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» answers|body|[object]|false|none|
|»» question_id|body|string|false|none|
|»» selected|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "correct_count": 0,
  "feedback": [
    {
      "question": "string",
      "correct_answer": "string",
      "selected_answer": "string"
    }
  ]
}
```

<h3 id="post__paanswers-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Evaluation results|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request parameters|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|None|

<h3 id="post__paanswers-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» correct_count|integer|false|none|none|
|» feedback|[object]|false|none|none|
|»» question|string|false|none|none|
|»» correct_answer|string|false|none|none|
|»» selected_answer|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__paimprovement

> Code samples

```shell
# You can also use wget
curl -X POST /paimprovement \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /paimprovement HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "feedback": [
    {
      "question": "string",
      "correct_answer": "string",
      "selected_answer": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/paimprovement',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/paimprovement',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/paimprovement', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/paimprovement', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/paimprovement");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/paimprovement", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /paimprovement`

*Provide improvement suggestions based on feedback*

> Body parameter

```json
{
  "feedback": [
    {
      "question": "string",
      "correct_answer": "string",
      "selected_answer": "string"
    }
  ]
}
```

<h3 id="post__paimprovement-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» feedback|body|[object]|false|none|
|»» question|body|string|false|none|
|»» correct_answer|body|string|false|none|
|»» selected_answer|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "improvements": "string"
}
```

<h3 id="post__paimprovement-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Improvement suggestions generated successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|No feedback provided|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|Inline|

<h3 id="post__paimprovement-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» improvements|string|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error|string|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__chat

> Code samples

```shell
# You can also use wget
curl -X POST /chat \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /chat HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "prompt": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/chat',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/chat',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/chat', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/chat', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/chat");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/chat", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /chat`

*Chat with AI*

> Body parameter

```json
{
  "prompt": "string"
}
```

<h3 id="post__chat-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» prompt|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "chat": "string"
}
```

<h3 id="post__chat-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Chat response generated successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|No prompt provided|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal server error|Inline|

<h3 id="post__chat-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» chat|string|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error|string|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

