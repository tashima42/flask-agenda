# Flask Agenda
___
## Dev
Before starting: 
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 migrations.py
python3 api.py
```
## Api
* Get all contacts: `GET https://localhost:5000/agenda`
  * Response:
    ```
    {
      "success": true,
      "agenda": [
        {
          "id": 1,
          "name": "Joao",
          "phone": "4383749294849",
          "phoneType": "Personal",
          "favorite": 0
        }
      ]
    }
    ```
* Add one contact:  `POST https://localhost:5000/agenda`
  * Request:
    ```
    {
      "name": "Luiz",
      "phone": "1293814082304",
      "phoneType": "Personal",
      "favorite": 1
    }
    ```
  * Response:
    ```
    {
      "success": true,
      "contact": {
        "name": "Joao",
        "phone": "91283338193",
        "phoneType": "Personal",
        "favorite": 0
      }
    }
    ```
* Delete one contact:  `DELETE https://localhost:5000/agenda/<contact_id>`
  * Response:
    ```
    {
      "success": true
    }
    ```