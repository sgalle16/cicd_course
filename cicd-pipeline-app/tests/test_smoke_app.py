import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

# Fixture para configurar el navegador (similar a las pruebas de aceptación)


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecuta sin interfaz gráfica
    options.add_argument("--no-sandbox")  # Necesario para algunos entornos
    # Necesario para algunos entornos
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_smoke_test(browser):
    """SMOKE TEST: Verifica carga básica y título."""
    # Lee la URL de producción desde una variable de entorno
    # Usar la variable de entorno APP_BASE_URL que inyectaremos en el pipeline con la URL del ALB de Producción
    app_url = os.environ.get("APP_BASE_URL", "http://localhost:5000")
    # Imprime para depuración
    print(f"Smoke test ejecutándose contra: {app_url}")
    try:
        browser.get(app_url + "/")
        print(f"Título de la página: {browser.title}")
        # Verifica que el título contenga "Calculadora"
        assert "Calculadora" in browser.title
        h1_element = browser.find_element(By.TAG_NAME, "h1")
        print(f"Texto H1: {h1_element.text}")
        assert h1_element.text == "Calculadora"  # Verifica el texto del H1
        print("Smoke test pasado exitosamente.")
    except Exception as e:
        print(f"Smoke test falló: {e}")
        # Opcional: tomar captura de pantalla si falla
        # browser.save_screenshot('smoke_test_failure.png')
        raise  # Vuelve a lanzar la excepción para que pytest marque el test como fallido
