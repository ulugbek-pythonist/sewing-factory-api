# sewing-factory-api
API for sewing factory

1. Clone project repo and change direction:<br/>
`git clone https://github.com/ulugbek-pythonist/sewing-factory-api.git`<br/>
`cd sewing-factory-api`
<br/>
2. Create virtual environment and activate it:<br/>
`python3 -m venv env`<br/>
`source env/bin/activate`<br/>

3. Install requirements:<br/>
`pip install -r requirements.txt`<br/>

4. Follow this command:<br/>
`python manage.py runserver`<br/>

5. Make requests:<br/>
GET: `http://127.0.0.1:8000/api/products/`

```
[
    {
        "id": 1,
        "created_at": "2024-03-20T04:21:50.653466Z",
        "updated_at": "2024-03-20T04:21:50.653481Z",
        "name": "Ko'ylak",
        "barcode": "123"
    },
    {
        "id": 2,
        "created_at": "2024-03-20T04:21:50.662399Z",
        "updated_at": "2024-03-20T04:21:50.662416Z",
        "name": "Shim",
        "barcode": "456"
    }
]
```

POST: `http://127.0.0.1:8000/api/material-requirements/`

```
{
"products": [
{"product_id":1,"quantity":30},
{"product_id":2,"quantity":20}
]
}
```

result is:

```
{
    "result": [
        {
            "product_name": "Ko'ylak",
            "product_qty": 30,
            "product_materials": [
                {
                    "warehouse_id": 1,
                    "material_name": "Mato",
                    "qty": 12,
                    "price": 1500
                },
                {
                    "warehouse_id": 2,
                    "material_name": "Mato",
                    "qty": 12,
                    "price": 1600
                },
                {
                    "warehouse_id": 5,
                    "material_name": "Tugma",
                    "qty": 150,
                    "price": 300
                },
                {
                    "warehouse_id": 3,
                    "material_name": "Ip",
                    "qty": 40,
                    "price": 500
                },
                {
                    "warehouse_id": 4,
                    "material_name": "Ip",
                    "qty": 260,
                    "price": 550
                }
            ]
        },
        {
            "product_name": "Shim",
            "product_qty": 20,
            "product_materials": [
                {
                    "warehouse_id": 2,
                    "material_name": "Mato",
                    "qty": 28,
                    "price": 1600
                },
                {
                    "warehouse_id": 4,
                    "material_name": "Ip",
                    "qty": 40,
                    "price": 550
                },
                {
                    "warehouse_id": null,
                    "material_name": "Ip",
                    "qty": 260,
                    "price": null
                },
                {
                    "warehouse_id": 6,
                    "material_name": "Zamok",
                    "qty": 20,
                    "price": 2000
                }
            ]
        }
    ]
}
```