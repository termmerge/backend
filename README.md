# 🌠 TermMerge (Backend API)
> Backend API platform for crowd-sourced word convergences - complements WordNet, which is continually updated and manually tooled by researchers.

## Purpose
This backend REST-ful API is the central service of the actual TermMerge platform. 

The main tasks of this API server are:
* **Creating** a data provider that can report a word convergence
* **Authenticating** a data provider
* **Obtaining** a reported word convergence
* **Getting** a real-time stream of reported convergences as they come in. 

## Tech Stack

The following technologies were used:

* 🐍 **Python 3.6** - Main programming language used on the API
* 🐋 **Docker** - Containerization for quick deployment
* 📊 **Neo4J** - Graph database for quick querying and graph processing
* 🗒️ **Postgres** - Relational database for normalized access

## Relational Schema

Data is stored on the relational database in normalized form, for allowing all sorts of other algorithms and computation work to be done on the raw data.

| user                  | report                    | word_timeline                     |
|-----------------------|---------------------------|-----------------------------------|
| **id** `varchar`      | **id** `varchar`          | **report_id** `foreign:report.id` |
| name `int`            | user_id `foreign:user.id` | **word** `string`                 |
| username `int`        | created_at `datetime`     | pre_word `string`                 |
| password `text`       | converge `string`         | post_word `string`                |
| created_at `datetime` |                           | epoch `int`                       |

## API Routes
The following are the API routes that can be accessed to utilize the backend API
	
  * `POST /user`
    * Create a data provider account provided a provider name, username and password. This will automatically generate a data provider id to identify the data provider with whenever reporting a word convergence.
    * Request Body: `{id:string, name:string,  username:string, password:string}`
    * Response Body: `None`
    
  * `GET /user`
  	* Get the list of data providers
    * Request Body: `None`
    * Response Body: `[{name:string, username:string, createdAt:string}]`
    
  * `GET /user/<username:string>`
  	* Get information about a specific provider
    * Request Body: `None`
    * Response Body: `{name:string, username:string, createdAt:string}`
    
  * `POST /auth`
  	* Provided a data provider username and password, return an authentication token that can be used to identify a data provider when it makes a word convergence response.
    * Request Body: `{username:string, password:string}`
    * Response Body: `{token:string}`
    
  * `POST /convergence`
  	* Report a word convergence.
    * Request Body: `{token:string, converge:string, branch1:[string], branch2:[string]}`
    * Response Body: `None`
    
  * `GET /convergence`
    * Obtain a URL containing a real-time web socket, which, when binded to, provides a real-time stream of incoming word convergences.
    * Request Body: `{socket:string}`
    * Response Body: `None`
