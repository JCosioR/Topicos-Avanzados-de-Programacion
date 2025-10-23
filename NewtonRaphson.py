# Metodo de Newton-Raphson
import sympy as sp

# --- Entrada ---
x = sp.Symbol('x')
expr_str = input("Ingresa la función f(x): "). strip().replace('^', '**')
f = sp.sympify(expr_str)
df = sp.diff(f, x)


"""Agregar un mensaje de error cuando
   se pidan más de 50 iteraciones""" 
"""
    Metodo de Broyden para resolver sistemas de ecuaciones no lineales F(x) = 0

    f: funcion vectorial que recibe un vector x y devuelve un vector f(x)
    x0: vector inicial (numpy array)
    tol: tolerancia para el criterio de convergencia
    max_iter: numero maximo de iteraciones
    """

fx = sp.lambdify(x, f, 'numpy')
dfx = sp.lambdify(x, df, 'numpy')
# Instrucciones iniciales
#print("Ingresa tu función en términos de x.")
#print("Ejemplos válidos:")
#print("  x**3 + 4*x**2 - 10")
#print("  sin(x) - 0.5")
#print("  exp(x) - 3")

x0 = float(input("Ingresa el valor inicial x0: "))
tol = float(input("Tolerancia (ej. 1e-5): "))
max_iter = int(input("Máx. iteraciones: "))
# Entrada y parsing
#expr_str = input("Función f(x):").strip()
#expr_str = expr_str.replace('^', '**')

# --- Iteraciones ---
for i in range(max_iter):
    f_x = fx(x0)
    df_x = dfx(x0)
    if df_x == 0:
        print("Derivada cero. No se puede continuar.")
        break
    x1 = x0 - f_x / df_x
    error = abs(x1 - x0)
    print(f"Iter {i+1}: x = {x1:.6}, error = {error:.2e}")
    if error < tol:
        print(f"\nConvergencia alcanzada en {i+1} iteraciones.")
        print(f"Raíz aproximada: {x1:.6f}")
        break
    x0 = x1
else:
    print("\nNo hubo convergencia.")
##    n = len(x0)
##    x = x0.astype(float)
##    B = np.eye(n) # matriz Jacobiana aproximada inicial
##    fx = f(x)
##
#    #x = sp.symbols('x')
#    #try:
#    #    expr = sp.sympify(expr_str)
#    #except (sp.SympifyError, Exception) as e:
#    #    print("No pude interpretar la expresión:", e)
#    #    raise SystemExit
#
# #   print (f"{'Iter': <5}{'x':<30}{'||f(x)||':<15}")
# #   print("-" * 60)
#
#    # Hepler para conversión segura
#    #def safe_float(value):
##
##   for k in range(max_iter):
##       # Resolver el sistema B * s = -f(x)
##       try:
##           s = np.linalg.solve(B, -fx)
##       except np.linalg.LinAlgError:
##           print("❌ La matriz B se volvió singular. No se puede continuar.")
##           break
##
##       x_new = x+s
##       fx_new = f(x_new)
#
## Intervalo
##while True:
##    try:    
##        a = float(input("Ingresa el límite inferior a: "))
##        b = float(input("Ingresa el límite superior b: "))
#    # Criterio de convergencia
#        # corregir orden si a > b, y rechazar si son iguales
#        if np.linalg.norm(fx_new, ord=2) < tol:
#            print(f"{k+1<5}{x_new}<15{np.linalg.norm(fx_new):.3e}")
#            print("\n✅ Convergencia alcanzada.")
#            return x_new

    # Actualización del Jacobiano aproximado (fórmula de Broyden)
#    if a == b:
#        print("⚠️ El intervalo tiene longitud 0. Ingresa a < b.\n")
#        continue
#        
#        try:
#            fa = safe_float(fx(a))
#            fb = safe_float(fx(b))
#        except Exception as e:
#            print(f"⚠️ Error evaluando la función en a o b: {e}\n")
#            continue
##
##        if fa * fb > 0:
##            raise ValueError("⚠️  Error: f(a) y f(b) tienen el mismo signo. Elige otro intervalo.\n")
##            continue
##        break   # Continúa si el intervalo es válido
#        y = fx_new - fx
#        B = B + np.outer((y - B @ s), s) / np.dot(s, s)#
##
#    # Imprimir iteracion
###    except ValueError:
###        print("⚠️ Entrada inválida. Ingresa solo números.\n")
###    except Exception as e:
###        print("⚠️ Error evaluando la función en a o b: {e}\n")
##        print(f"{k+1<5}{x_new}<15{np.linalg.norm(fx_new):.3e}")        #
##
## Criterio de paro
###modo = input("Criterio de paro: (t)olerancia o (n) iteraciones?: [t/n]").strip().lower()
###if modo == 't':
###    tol = float(input("tol = (ej. 1e-4) ="))
###    max_iter = int(input("max_iter (seguridad) = "))
###else:
###    tol = None
###    max_iter = int(input("n_iter = "))
##    # Actualizar variables para la siguiente iteracion
##        x = x_new
##        fx = fx_new#
##
#    print ("\n⚠️ No convergió tras", max_iter, "iteraciones.")
##    return x
#### Bisección
###rows = []
###i = 1
###c_prev = None
###reason = None
##    """
##    Ejemplo de uso:
##    Sistema:
##    f1(x, y) = x^2 + y^2 - 4 = 0
##    f2(x, y) = x * y - 1 = 0
##    """
###while True:
###    c = (a + b) / 2.0
###    fa = safe_float(fx(a))
###    fb = safe_float(fx(b))
###    fc = safe_float(fx(c))
###    error = None if c_prev is None else abs(c - c_prev)
###    rows.append([i, a, b, c, fa, fc, fb, error])#
##
##def F(v):
##    x, y = v
##    return np.array([
##        x**2 + y**2 - 4,
##        x * y - 1
##    ])#
##
##    if fc == 0:
###        reason = 'fc == 0 (raíz exacta)'
###        break
###    if tol is not None:
###        if error is not None and error < tol:
###            reason = f'error < {tol}'
###            break
###        if abs(b - a) < tol:
###            reason = f'error <{tol}'
##            break
##    if i >= max_iter:
##        reason = 'max_iter alcanzado'
##        break
#    
#x0 = np.array([2.0, 0.5])
#sol = broyden(F, x0)
##    if fa * fc < 0:
##        b = c
##    else:
##        a = c#
#
#print("\nSolución aproximada:", sol)
##    c_prev = c
##    i += 1
##
### Presentar resultados
##df = pd.DataFrame(rows, columns=['iter', 'a', 'b', 'c', 'f(a)', 'f(c)', 'f(b)', 'error'])
##df_display = df.copy()
##for col in ['iter', 'a', 'b', 'c', 'f(a)', 'f(b)', 'error']:
##    df_display[col] = df_display[col].apply(lambda v: f"{v:.6e}" if pd.notnull(v) else "")
##
##xi = np.linspace(rows[0][1], rows[0][2], 300)
##fi = fx(xi)
##
##fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), gridspec_kw={'height_ratios': [3, 1]})
##ax1.plot(xi, fi)
##ax1.axhline(0, linewidth=0.8)
##root_approx = df['c'].iloc[-1]
##ax1.plot(root_approx, df['f(c)'].iloc[-1], 'o', label=f'c ≈ {root_approx:.6f}')
##ax1.set_title(f'Bisección - raíz aproximada: {root_approx:.6f} ({reason})')
##ax1.legend()
##ax2.axis('off')
##table = ax2.table(cellText=df_display.values, colLabels=df_display.columns, loc='center')
##table.auto_set_font_size(False)
##table.set_fontsize(8)
##table.scale(1, 1.2)
##plt.tight_layout()
##plt.show(#)