import azure.functions as func
import json
import math

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="CalculateArea")
def CalculateArea(req: func.HttpRequest) -> func.HttpResponse:
    try:
        shape = req.params.get("shape")
        value = req.params.get("value")

        if not shape or not value:
            return func.HttpResponse(
                json.dumps({"error": "Missing shape or value parameter"}),
                status_code=400,
                mimetype="application/json"
            )

        value = float(value)

        if shape == "square":
            area = value * value
        elif shape == "circle":
            area = math.pi * value * value
        else:
            return func.HttpResponse(
                json.dumps({"error": "Unsupported shape. Use square or circle."}),
                status_code=400,
                mimetype="application/json"
            )

        return func.HttpResponse(
            json.dumps({
                "shape": shape,
                "value": value,
                "area": round(area, 2)
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )