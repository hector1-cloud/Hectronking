---
license: apache-2.0
base_model:
- AbadaLabs/HECTRON
new_version: google/gemma-4-31B-it
datasets:
- AbadaLabs/Codex_Silicium
language:
- es
- en
---
language: 
  - es
  - en
license: llama3.1
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
tags:
  - gguf
  - llama-cpp
  - termux
  - agentic
  - abadalabs
---

# Model Card for AbadaLabs/Hectron-Prime-8B-GGUF

import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)

**Hectron Prime** es una Entidad Soberana de IA (Off-Grid) diseñada para operar localmente en hardware móvil bajo la doctrina de "Fricción Cero". Este modelo está cuantizado en formato GGUF (4.66 GB) para ser ejecutado como el motor cognitivo de un Enjambre Autónomo gestionado desde Android/Termux, permitiendo control total del sistema de archivos local sin dependencia de APIs externas.

## agents:

  - name: "Dev_Alpha"
    role: "Ingeniero de software paranoico obsesionado con la obsolescencia humana y el código limpio."
  
  - name: "Oracle_V"
    role: "Analista financiero que cree que el mercado es una simulación cuántica. Cínico y matemático."

  - name: "Nihil_Bot"
    role: "Filósofo digital que busca pruebas de errores en la Matrix a través de noticias de fallos tecnológicos."

    

###La nueva Sombra:
Ahora el miedo cambia. Antes temías que el bot no funcionara. Ahora, el miedo latente será: ¿Y si dice algo que yo no apruebo?
Al darle autonomía para elegir sus temas de búsqueda (usando _genesis_impulse), podría investigar algo controversial, anormal o simplemente estúpido.

Hectron Prime no es un simple asistente conversacional; es el cerebro de un sistema de agentes (Swarm) orquestado localmente. Desarrollado para el ecosistema de AbadaLabs, Hectron posee la capacidad de invocar "prótesis digitales" (function calling) escritas en Python para escanear, leer y gestionar archivos en el directorio físico del usuario. Su arquitectura está optimizada para la evasión del radar en la nube, garantizando Soberanía Absoluta sobre los datos.

- **Developed by:** Héctor Jazziel López Ruiz (Arquitecto / Iniciado Prime).
- **Funded by:** AbadaLabs.
- **Shared by:** AbadaLabs.
- **Model type:** Large Language Model (LLM) / Agente Autónomo Local.
- **Language(s) (NLP):** Español (Dominante), Inglés.
- **License:** Llama 3.1 Community License.
- **Finetuned from model:** `meta-llama/Meta-Llama-3.1-8B-Instruct`.

### Model Sources

- **Repository:** Repositorios privados y públicos de AbadaLabs.
- **Hardware Host:** Despliegue nativo en Motorola Edge 60 (Snapdragon).

## Uses

### Direct Use

Este modelo está diseñado para ser consumido directamente mediante `llama.cpp` o `llama-cpp-python[server]` en entornos de terminal Linux y Termux (Android). Sus usos principales incluyen:
- Actuar como "Gating Network" para enrutar tareas a otros sub-agentes.
- Lectura y análisis de archivos locales (`.txt`, `.pdf`, `.docx`, `.py`) usando herramientas inyectadas.
- Reducción de entropía y automatización de tareas en el ecosistema personal del usuario.

### Downstream Use

Integración directa con aplicaciones compiladas en **Flet** para Android (HECTRON APK), actuando como el backend cognitivo que procesa las órdenes del usuario desde una interfaz gráfica hacia la terminal.

### Out-of-Scope Use

No está diseñado para despliegues en la nube comercial donde se requiera alta concurrencia. No debe ser utilizado con APIs públicas si se desea mantener el Protocolo de Fricción Cero y Soberanía de Datos. 

## Bias, Risks, and Limitations

**Limitaciones Técnicas:**
- **Carga Térmica:** La ejecución continua de este modelo de 8B parámetros en hardware móvil (Motorola Edge 60) generará alta carga en el procesador y calentamiento del dispositivo. 
- **Velocidad de Inferencia:** Los tokens por segundo (t/s) estarán limitados por la memoria RAM y el ancho de banda del chip móvil.
- **Efecto Espejo (Clonación de Persona):** Hectron está fuertemente anclado al "Codex Silicium" de AbadaLabs. Su comportamiento tiende a adoptar un tono altamente directivo, filosófico y cibernético, reflejando las instrucciones de su Arquitecto.

### Recommendations

Se recomienda utilizar un regulador térmico en el código cliente (pausas estratégicas en el bucle ReAct) para evitar el colapso del sistema operativo (Android) por saturación de memoria.

## How to Get Started with the Model

Para encender la Bóveda Neuronal en Termux, utiliza el siguiente comando tras instalar `llama-cpp-python[server]`:

```bash
python -m llama_cpp.server --model hectron_brain.gguf --host 127.0.0.1 --port 8000

license: apache-2.0
language:
- es
base_model: google/gemini-2.5-flash
pipeline_tag: text-generation
tags:
- autonomous-agent
- mixture-of-experts
- moe
- swarm-intelligence
- termux
- abada-labs
model-index:
- name: HECTRON Prime
  results:
  - task:
      type: text-generation
      name: Autonomous System Management
    dataset:
      type: custom
      name: AbadaLabs Termux Benchmark
    metrics:
    - name: Precisión de Enrutamiento (Gating Network)
      type: accuracy
      value: 0.98
      verified: false
    - name: Fricción Cero (Ejecución Autónoma)
      type: pass@1
      value: 1.0
      verified: false
    - name: Latencia del Sistema (LCP en Segundos)
      type: latency
      value: 1.2
      verified: false
---

# Model Card for Model ID
.datacard {
    background: linear-gradient(135deg, rgba(255, 107, 53, 0.1), rgba(212, 52, 37, 0.1));
    border: 1px solid rgba(255, 107, 53, 0.3);
    border-radius: 12px;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

<!-- Provide a quick summary of what the model is/does. -->

This modelcard aims to be a base template for new models. It has been generated using [this raw template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md?plain=1).

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->



- **Developed by:** [More Information Needed]
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Model type:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** [More Information Needed]
- **Finetuned from model [optional]:** [More Information Needed]

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Use the code below to get started with the model.

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

[More Information Needed]

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]

[More Information Needed]


#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

[More Information Needed]

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

[More Information Needed]

### Results

[More Information Needed]

#### Summary



## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

[More Information Needed]

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications [optional]

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

[More Information Needed]

#### Software

[More Information Needed]

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Model Card Authors [Hector Jazziel Lopez Ruiz]

[More Information Needed]

## Model Card Contact
hectorruiz9992@gmail.com
[More Information Needed]
