from fastapi import FastAPI, HTTPException
from models.request_models import PowRequest, FibonacciRequest, FactorialRequest
from services.math_service import power, fibonacci, factorial
from storage.db import init_db, log_request

import uvicorn

app = FastAPI(title="Math Microservice API")

# Initializare baza de date
init_db()


@app.post("/pow")
async def calculate_power(request: PowRequest):
    try:
        result = await power(request.base, request.exponent)
        log_request("pow", f"base={request.base}, exp={request.exponent}", str(result))
        return {"operation": "pow", "input": request.dict(), "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/fib")
async def calculate_fibonacci(request: FibonacciRequest):
    try:
        result = await fibonacci(request.n)
        log_request("fibonacci", f"n={request.n}", str(result))
        return {"operation": "fibonacci", "input": request.dict(), "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/fact")
async def calculate_factorial(request: FactorialRequest):
    try:
        result = await factorial(request.n)
        log_request("factorial", f"n={request.n}", str(result))
        return {"operation": "factorial", "input": request.dict(), "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Pentru rulare locală:
if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
