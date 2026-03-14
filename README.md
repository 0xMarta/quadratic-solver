# quadratic-solver

# Quadratic Solver & Visualizer 📈

Projekt edukacyjny do rozwiązywania równań kwadratowych z wizualizacją wyników. Skrypt analizuje wprowadzone równanie, wylicza deltę oraz pierwiastki, a następnie rysuje wykres funkcji.

## 🛠️ Co musisz zainstalować?

Zanim uruchomisz program, musisz zainstalować niezbędne biblioteki (NumPy do obliczeń i Matplotlib do wykresów). Otwórz terminal i wpisz:

```bash
pip install numpy matplotlib
```

## 📝 Instrukcja wpisywania równania

Program wymaga konkretnego formatu, aby poprawnie odczytać współczynniki `a`, `b` i `c`.

**Zasady:**
- **Format:** `ax^2+/-bx+/-c`
- **Bez spacji:** Całe równanie musi być jednym ciągiem znaków.
- **Współczynnik 1:** Jeśli przy `x` nie ma liczby, **zawsze wpisz 1** (np. zamiast `x^2`, wpisz `1x^2`).

**Przykłady poprawnych wpisów:**
- `1x^2+6x-9`
- `2.5x^2-6x+9`
- `1x^2-4x+4`
- `-2x^2+8x-1`
