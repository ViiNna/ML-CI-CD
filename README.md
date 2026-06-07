W zadaniu 3 użyłam w linii komned cURL: curl -X POST https://ntpdlab5-89255163278.europe-central2.run.app/predict   -H "Content-Type: application/json"   -d '{"value": 5}'

i otrzymałam wynik: {"prediction":[10.0]}


Porównanie dla Zadania 4: 

Google Cloud Run

- Brak zarządzania infrastrukturą

- Automatyczne skalowanie

- Płatność tylko za czas działania

- Ograniczenia czasu i zasobów

- Mniejsza kontrola nad środowiskiem


Własny serwer

- Pełna kontrola

- Niższe koszty przy dużym ruchu

- Brak limitów środowiskowych

- Konieczność aktualizacji, monitoringu, skalowania





w zadaniu 5 użyłam: 

gcloud run deploy ntpdlab5   --image gcr.io/i-informatics-498721-j3/ntpdlab5:v1   --platform managed   --region europe-central2   --allow-unauthenticated


gcloud run deploy ntpdlab5 \
  --image gcr.io/i-informatics-498721-j3/ntpdlab5:v1 \
  --platform managed \
  --region europe-central2 \
  --allow-unauthenticated \
  --set-env-vars KEY=TEST_KEY



i do testowania użyłam w linii komend cURL: curl https://ntpdlab5-89255163278.europe-central2.run.app/config

i otrzymałam wynik: {"key":"TEST_KEY"}
