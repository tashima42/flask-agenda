# Flask Agenda
___
## Dev
Before starting: 
```bash
pip install virtualenv          # Install virtual enviroment tool
virtualenv venv                 # Start a virtual environment
source venv/bin/activate        # Activate virtual environment
pip install -r requirements.txt # Install requirements
python3 migrations.py           # Run migrations
python3 controller.py           # Run server
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