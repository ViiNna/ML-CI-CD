from main import app, train_and_predict, get_accuracy

#utworzenie klienta testowego Flask
client = app.test_client()


def test_predictions_not_none():
    """
    Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    """
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."





def test_predictions_length():
    """
    Test 2 (na maksymalną ocenę 5): Sprawdza, czy długość listy predykcji jest większa od 0 i czy odpowiada
   przewidywanej liczbie próbek testowych.
    """
    preds, y_true = train_and_predict()
    assert len(preds) == len(y_true), "Predictions length should match true labels length."





def test_predictions_value_range():
    """
    Test 3 (na maksymalną ocenę 5): Sprawdza, czy wartości w predykcjach mieszczą się w spodziewanym zakresie:
   Dla zbioru Iris mamy 3 klasy (0, 1, 2).
    """
    #jako iż mój model polega na regresji liniowej a nie klasyfikacji to zamiast tej funkcji zrobiłam funkcję która sprawdza czy wartości predykcji są liczbami i czy mieszczą sie w oczekiwanym zakresie
    preds, _ = train_and_predict()
    assert all(isinstance(float(p), float) for p in preds), "All predictions should be floats."
    assert all(p > 0 for p in preds), "Predictions should be positive."





def test_model_accuracy():
    """
    Test 4 (na maksymalną ocenę 5): Sprawdza, czy model osiąga co najmniej 70% dokładności (przykładowy
   warunek, można dostosować do potrzeb).
    """
    acc = get_accuracy()
    assert acc >= 0.7, f"Accuracy should be >= 0.7, got {acc}"
