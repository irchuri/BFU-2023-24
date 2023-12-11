import requests as req

# Открываем файл для записи результатов запросов
with open('requests_results.txt', 'w') as file:

    request1 = req.get('https://httpbin.org/get')
    file.write(f"--- Request 1 ---\n")
    file.write(f"status_code: {request1.status_code}\n")
    file.write(f"headers: {request1.headers}\n")
    file.write(f"text: {request1.text}\n\n")

    request2 = req.get('https://httpbin.org/get')
    file.write(f"--- Request 2 ---\n")
    file.write(f"status_code: {request2.status_code}\n")
    file.write(f"headers: {request2.headers}\n")
    file.write(f"text: {request2.text}\n\n")

    request3 = req.get('https://httpbin.org/get')
    file.write(f"--- Request 3 ---\n")
    file.write(f"status_code: {request3.status_code}\n")
    file.write(f"headers: {request3.headers}\n")
    file.write(f"text: {request3.text}\n\n")
    file.write(f"allowed headers: {request3.headers['Allow']}\n")
