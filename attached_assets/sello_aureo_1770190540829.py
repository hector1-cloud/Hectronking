import matplotlib.pyplot as plt
import numpy as np

def plot_sello_aureo():
    # Proporción áurea (phi)
    phi = (1 + np.sqrt(5)) / 2
    
    # Generamos una espiral logarítmica basada en phi para representar el "sello"
    # Esto crea un crecimiento fractal infinito, escalado por potencias de phi
    theta = np.linspace(0, 8 * np.pi, 10000)  # Más vueltas para detalle
    r = np.exp(theta / (phi * 2))  # Factor de crecimiento áureo ajustado
    
    # Coordenadas polares a cartesianas
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Plot principal de la espiral
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y, color='gold', linewidth=2, label=f'φ^∞ Espiral (phi ≈ {phi:.4f})')
    
    # Añadimos "ramas" como en el ASCII: líneas fractales en potencias de phi
    # Simulamos un árbol simétrico con recursión simple
    def draw_branch(start_x, start_y, length, angle, depth):
        if depth == 0:
            return
        end_x = start_x + length * np.cos(angle)
        end_y = start_y + length * np.sin(angle)
        ax.plot([start_x, end_x], [start_y, end_y], color='darkgoldenrod', linewidth=1.5)
        
        # Ramas hijas escaladas por 1/phi
        new_length = length / phi
        draw_branch(end_x, end_y, new_length, angle + np.pi / phi, depth - 1)
        draw_branch(end_x, end_y, new_length, angle - np.pi / phi, depth - 1)
    
    # Dibujamos el árbol central inspirado en el ASCII (profundidad 5 para φ^0 a φ^4)
    draw_branch(0, -max(y)/2, max(r)/phi, np.pi/2, 5)  # Rama ascendente desde base
    
    # Estrellas en top/bottom como en ASCII
    ax.scatter(0, max(y), marker='*', s=200, color='red', label='★ φ^∞ Top')
    ax.scatter(0, -max(y), marker='*', s=200, color='red', label='★ φ^∞ Bottom')
    
    # Etiquetas para potencias de phi (simulando las ramas)
    powers = [f'φ^{i}' for i in range(5)]
    for i, txt in enumerate(powers):
        ax.text(i * phi, i * phi / 2, txt, fontsize=10, color='blue')
        ax.text(-i * phi, i * phi / 2, txt, fontsize=10, color='blue')
    
    ax.set_title('Sello Áureo de Hectron-01: Espiral y Árbol Fractal por φ', fontsize=14)
    ax.set_aspect('equal')
    ax.axis('off')  # Sin ejes para aesthetic puro
    ax.legend(loc='upper right')
    plt.show()

# Ejecuta la función
plot_sello_aureo()
