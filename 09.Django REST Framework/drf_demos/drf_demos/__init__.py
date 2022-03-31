"""
REST Representational State Transfer
API Application Programming Interface

- defines:
   - how other components/systems can use it
   - kind of calls or request that can be made

- can provide extension mechanism of extending existing functionalities

Models:
Category

REST API
    - JSON CRUD over categories
    - GET /api/categories -> list of categories
        /api/categories?order_by=name
        - ListAPIView

    - GET /api/categories/{ID} -> details of a category
        - RetrieveAPIView

    - POST /api/categories/{ID} -> creates a category
        - CreateAPIView

    - PUT /api/categories/{ID} ->  updates a category
        - UpdateAPIView

    - DELETE /api/categories/{ID} -> deletes a category
        - DestroyAPIView

REST gives unified way to work with the backend.

   # With REST
      - Android app, frontend with Java/Kotlin
      - Web app, frontend with React

   # Without REST
      - Web app with only server-side rendering
      - Android app with JSON APIs

# Data with Server-side rendering (forms):
  -  <form method="GET/POST">

# Data with JSON API(rest):
  -  POST/GET
  -  PUT, DELETE, PATCH, HEAD, ...

"""
