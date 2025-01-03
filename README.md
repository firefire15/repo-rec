# SOFTWARE PROGRAMMER - BACKEND ENGINEER (FOR CANDIDATES)
## _Program ini merupakan hasil pengerjaan dari soal https://wiki.digitalservice.id/s/61b126c8-01e3-4697-8765-6ec62b1c55ed#h-instruction_

# Features and Concepts
1. Program ini terdiri dari beberapa modul yakni apps, controller, database, dan model. Pembagian modul ini terinspirasi dari Model View Controller (MVC) Pattern yang memisahkan antara view (tampilan            antarmuka, Controller (operasi program) dan Model (kelas-kelas dan operasi database. Pada modul apps berisi dua file yakni file authenticate and fetch. File tersebut berisi endpoint untuk masing-masing       fungsi pada soal 1 yakni authenticate module dan soal 2 yakni fetch module.
2. Modul lain yakni controller yang berfungsi untuk menjembatani antara module apps dan koneksi ke database. Fungsi controller sendiri untuk membuat data balikan (return) yang nanti akan disebrangkan oleh       endpoint pada module apps. Sementara itu, module database berfungsi untuk menyimpan query atau fungsi untuk memanipulasi data pada database. Sementara modul model digunakan untuk menunjang module             database berupa kelas-kelas. 
3. Endpoint ini dapat dijalankan pada port yang berbeda, untuk menjalankan endpoint ini dapat menggunakan perintah python authenticate.py --port 8080 untuk authenticate apps dan python fetch.py --port 8080      untuk fetch apps. Keduanya dijalankan pda localhost untuk port 8080. Port 8080 dapat diubah ke alamat port yang lain sesuai kebutuhan. Kondisi port default adalah port 5000.
4. Database yang digunakan adalah mysql dengan nama 'rec_jds' yang memiliki dua tabel tabel user dan tabel product. Adapun tabel user memiliki beberapa atribut yaitu:id, nik, role password, sedangkan tabel      product memiliki atribut yaitu: :id, product, department, price, idr_price, created_at. Sementara itu untuk data koneksi python ke mysql adalah sebagai berikut: host='localhost',  user='root',          
   password='',  database='rec_jds'.

# API Documentation
## _Adapun dokumentasi API adalah sebagai berikut:_

### apps authenticate:
#### Generating user
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```sh
info:
  title: Generating user
  description: API to generate user based on NIK and role.
  version: 1.0.0
servers:
  - url: http://localhost:XXXX
    description: Local server
paths:/generate_user:
    get:
      summary: Generate password on 6 character length based on nik and role, after that save to database 
      description: retrieve two post data (nik and role) and returning JSON object with nik, role, and generating password.
	request : 
		field: nik
			type : string
			method: POST
		field: role
			type : string
			method: POST
    responses:
        200:
          description: Successful response with the JSON return.
          content:
            application/json:
              schema:
                type: object
                properties:
                  nik:
                    type: string
                    format: -
                    description: nik (nomor induk kependudukan) which enter by user. Usually the length is 16 characters [0-9].
                    example: 3322771612750008
		              role:
                    type: string
                    format: -
                    description: user role in application (admin, superadmin etc).
                    example: admin
		              password:
                    type: string
                    format: -
                    description: user password in 6 character.
                    example: abcdef

        500:
          description: Internal server error.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message when NIK or role are missing.
                    example: parameters NIK and role are required.
		              error:
                    type: string
                    description: Error message when NIK is not 16 characters [0-9].
                    example: parameters NIK and role are required.
```
#### Login user
-------------------------------------------------------------------------------------------------------------------------------------------------------
```sh
info:
  title: Login User
  description: API to authenticate User Login
  version: 1.0.0
servers:
  - url: http://localhost:XXXX
    description: Local server
paths:
  /login:
    get:
      summary: this endpoint retrieve nik and password from user
      description: retrieveing nik and password from user. Program will match the password in database
	request : 
		field: nik
			type : string
			method: POST
		field: password
			type : string
			method: POST

      responses:
        200:
          description: Successful response with the JSON return.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    format: -
                    description: unique id .
                    example: 4d761d9e-2ffe-47ee-93f6-0ba84bad477b
                  nik:
                    type: string
                    format: -
                    description: nik (nomor induk kependudukan) which enter by user. Usually the length is 16 number character [0-9].
                    example: 3322771612750008
                  role:
                    type: string
                    format: -
                    description: user role in application (admin, superadmin etc).
                    example: admin
                  password:
                    type: string
                    format: -
                    description: user password in 6 character.
                    example: abcdef
                  jwt:
                    type: string
                    format: -
                    description: generate token after authenticate.
                    example: rep0ojk*ubl9DRY8nbn


        500:
          description: Internal server error.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message when NIK or passoword are missing.
                    example: parameters NIK and role are required.
                  error:
                    type: string
                    description: Error message when NIK is not 16 number character [0-9].
                    example: parameters NIK and role are required.
                  error:
                    type: string
                    description: Error message when NIK or password are wrong [0-9].
                    example: login failed, wrong password or NIK.
```
#### User data
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```sh
info:
  title: Userdata
  description: API to get private user data
  version: 1.0.0
servers:
  - url: http://localhost:XXXX
    description: Local server
paths:
  /login:
    get:
      summary: this endpoint retrieve nik and jwt token from user
      description: retrieveing nik and jwt token from user session. Program will display the private data from user. 
	request : 
		field: nik
			type : string
			method: POST
		field: jwt
			type : string
			method: POST

      responses:
        200:
          description: Successful response with the JSON return.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    format: -
                    description: unique id .
                    example: 4d761d9e-2ffe-47ee-93f6-0ba84bad477b
                  nik:
                    type: string
                    format: -
                    description: nik (nomor induk kependudukan) which enter by user. Usually the length is 16 number character [0-9].
                    example: 3322771612750008
                  role:
                    type: string
                    format: -
                    description: user role in application (admin, superadmin etc).
                    example: admin
                  password:
                    type: string
                    format: -
                    description: user password in 6 character.
                    example: abcdef
                  jwt:
                    type: string
                    format: -
                    description: generate token after authenticate.
                    example: rep0ojk*ubl9DRY8nbn
        500:
          description: Internal server error.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message when JWT token is invalid.
                    example: Invalid JWT Token.
```
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### apps fetch

#### Fetch data
```sh
info:
  title: fetch_data
  description: API to fetch data from external API
  version: 1.0.0
servers:
  - url: http://localhost:XXXX
    description: Local server
paths:
  /login:
    get:
      summary: this endpoint just retrieve jwt token from user and return data from another API
      description: retrieving jwt token from user session. Program will display the data from another API. 
	request : 
		field: jwt
		type : string
		method: GET/POST

      responses:
        200:
          description: Successful response with the JSON return.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    format: -
                    description: unique id .
                    example: 1
                  product:
                    type: string
                    format: -
                    description: name of product or goods.
                    example: Salad
                  department:
                    type: string
                    format: -
                    description: department of product.
                    example: outdoor
                  price:
                    type: double
                    format: x.00
                    description: price of product in USD.
                    example: 218.0
                  idr_price:
                    type: double
                    format: x.00
                    description: price of product in IDR.
                    example: 3535524.0
                  createdAt:
                    type: Date
                    format: yyyy-mm-ddTHH:MM:ssZ
                    description: timestamp
                    example: 2021-06-09T09:37:05.527Z
                  jwt:
                    type: string
                    format: -
                    description: generate token after authenticate.
                    example: rep0ojk*ubl9DRY8nbn


        500:
          description: Internal server error.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message when JWT token is invalid.
                    example: Invalid JWT Token.
```
#### Aggregate data
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```sh
info:
  title: aggregate_data
  description: API to aggeregate data from database
  version: 1.0.0
servers:
  - url: http://localhost:XXXX
    description: Local server
paths:
  /login:
    get:
      summary: this endpoint retrieve jwt token and role from user and return data from database query
      description: retrieving jwt token and role from user session. Program will display the data from database query. 
	request : 
	     field: jwt
		type : string
		method: GET/POST
	     field: role
		type : string
		method: GET/POST


      responses:
        200:
          description: Successful response with the JSON return.
          content:
            application/json:
              schema:
                type: object
                properties:
                  product:
                    type: string
                    format: -
                    description: name of product or goods.
                    example: Salad
                  department:
                    type: string
                    format: -
                    description: department of product.
                    example: outdoor
                  idr_price:
                    type: double
                    format: x.00
                    description: price of product in IDR after aggregation with product and department.
                    example: 3535524.0

        500:
          description: Internal server error.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message when role is not 'admin'.
                    example: Invalid role.
                  error:
                    type: string
                    description: Error message when JWT token is invalid.
                    example: Invalid JWT Token.
```
#### User Data
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```sh
info:
  title: Userdata
  description: API to get private user data
  version: 1.0.0
servers:
  - url: http://localhost:XXXX
    description: Local server
paths:
  /login:
    get:
      summary: this endpoint retrieve nik and jwt token from user
      description: retrieveing nik and jwt token from user session. Program will display the private data from user. 
	request : 
		field: nik
			type : string
			method: POST
		field: jwt
			type : string
			method: POST

      responses:
        200:
          description: Successful response with the JSON return.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    format: -
                    description: unique id .
                    example: 4d761d9e-2ffe-47ee-93f6-0ba84bad477b
                  nik:
                    type: string
                    format: -
                    description: nik (nomor induk kependudukan) which enter by user. Usually the length is 16 number character [0-9].
                    example: 3322771612750008
                  role:
                    type: string
                    format: -
                    description: user role in application (admin, superadmin etc).
                    example: admin
                  password:
                    type: string
                    format: -
                    description: user password in 6 character.
                    example: abcdef
                  jwt:
                    type: string
                    format: -
                    description: generate token after authenticate.
                    example: rep0ojk*ubl9DRY8nbn


        500:
          description: Internal server error.
          content:
            application/json:
              schema:
                type: object
                properties:
		          error:
                    type: string
                    description: Error message when JWT token is invalid.
                    example: Invalid JWT Token.
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



