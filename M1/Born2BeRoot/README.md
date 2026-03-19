*Este proyecto ha sido creado como parte del currículo de 42 por jovillal.*

# Born2beroot

## 📌 Descripción

**Born2beroot** es un proyecto del cursus de 42 cuyo objetivo es introducir al estudiante en la administración básica de sistemas Linux y en los principios fundamentales de la seguridad informática.

El proyecto consiste en configurar una máquina virtual desde cero, siguiendo una serie de normas estrictas de seguridad. Durante el proceso se trabajan conceptos como:
- Instalación y configuración de un sistema operativo
- Gestión de usuarios y grupos
- Políticas de seguridad
- Servicios del sistema
- Firewall
- Uso de sudo
- Buenas prácticas en entornos Linux

El resultado final es un sistema estable, seguro y correctamente configurado.

---

## 🖥️ Elección del Sistema Operativo

Para este proyecto se ha utilizado **Debian** como sistema operativo.

### 🟢 Debian – Ventajas
- Gran estabilidad
- Amplia documentación y comunidad
- Sistema ligero y fiable
- Ideal para servidores y entornos de producción

### 🔴 Debian – Desventajas
- Paquetes más conservadores (no siempre las versiones más recientes)
- Menor orientación empresarial que Rocky Linux

---

## 🔄 Comparaciones Requeridas

### Debian vs Rocky Linux

| Debian | Rocky Linux |
|------|------------|
| Comunidad muy amplia | Orientado a entornos empresariales |
| Paquetes estables | Mayor compatibilidad con software empresarial |
| Más ligero | Más pesado |
| Ideal para aprendizaje | Ideal para producción corporativa |

---

### AppArmor vs SELinux

| AppArmor | SELinux |
|--------|---------|
| Más sencillo de configurar | Más potente y granular |
| Basado en perfiles | Basado en políticas |
| Mejor para principiantes | Curva de aprendizaje elevada |
| Usado en Debian | Usado en Rocky Linux |

En este proyecto se utiliza **AppArmor**, ya que es más accesible y está integrado de forma nativa en Debian.

---

### UFW vs firewalld

| UFW | firewalld |
|----|-----------|
| Configuración simple | Configuración avanzada |
| Ideal para principiantes | Más flexible |
| Reglas claras y directas | Zonas y servicios |
| Usado en Debian | Usado en Rocky Linux |

Se ha elegido **UFW** por su simplicidad y claridad.

---

### VirtualBox vs UTM

| VirtualBox | UTM |
|-----------|-----|
| Multiplataforma | Optimizado para macOS |
| Muy extendido | Mejor integración en Apple Silicon |
| Amplia documentación | Interfaz moderna |

En este proyecto se ha utilizado **VirtualBox** por su compatibilidad multiplataforma y su uso extendido en 42.

---

## ⚙️ Decisiones Técnicas Principales

- **Particionado**: uso de LVM para una gestión flexible del almacenamiento.
- **Seguridad**:
  - Contraseñas fuertes
  - Políticas estrictas de `sudo`
  - AppArmor activo
- **Gestión de usuarios**:
  - Usuario principal sin privilegios de root
  - Uso controlado de sudo
- **Servicios instalados**:
  - SSH
- **Firewall**:
  - UFW configurado con reglas básicas de seguridad

---

## 🛠️ Instrucciones

### ▶️ Ejecución

El proyecto no requiere compilación.  
La evaluación consiste en:

- Arrancar la máquina virtual
- Iniciar sesión correctamente
- Demostrar el funcionamiento de:
  - SSH
  - sudo
  - Firewall
  - Políticas de seguridad
  - Scripts requeridos

---

## 📚 Recursos

### Referencias utilizadas

- Documentación oficial de Debian
- Manuales de Linux (`man`)
- Linux Filesystem Hierarchy Standard
- Documentación de AppArmor
- Documentación de UFW
- Guías oficiales de VirtualBox

---

### 🤖 Uso de Inteligencia Artificial

La inteligencia artificial se ha utilizado únicamente como **herramienta de apoyo teórico**, para:

- Comprender conceptos de administración de sistemas
- Aclarar dudas sobre configuraciones de seguridad
- Entender el funcionamiento de servicios y políticas del sistema
- Ayudar a generar este README.md

Todo el trabajo práctico de configuración ha sido realizado manualmente, siguiendo la documentación oficial y las normas del proyecto.

---
