# Craft Home LAB with Ollama

---

## Introduction

This lab will guide you through the installation and use of local LLM models with Ollama. The goal is to learn how to run AI models locally, integrate them with Open-WebUI, and compare the performance of different models.

### Environment

Each student has their own set of two PODs accessible via URL to web terminal - just change XX to your student number (for example '07'). No password rquired. CPU-xx for Lab A and gpu-xx for Labs B,C,... The URL's are here for example

```
https://www.github.com/petrhanakcz/ollamalab/studentfiles/student-01.txt
```

### Work on your Laptop/VM

You can also work on any (Windows/Linux/Mac) laptop or virtual machine. But you have to adjust steps in this document

*!!! Especially for LAB A I suggest to use your laptop. The performance of CPU-POD is poor !!!*

### What You Will Learn

- Install Ollama on a Linux system
- Work with local LLM models (qwen, llama)
- Use the Ollama REST API
- Integrate Ollama with Open-WebUI
- Compare performance and quality of different models
- Bonus: LABs just as a inspiration for you what to test next

---

## Lab A - Ollama Installation and Working with Local LLMs

### Objective

Install Ollama, download several models of different sizes, and compare their performance.

### Exercise 1 - Environment Preparation

#### Step 1: Login to Shell

Login to shell via web browser. You can open multiple terminal instances at once - this will be useful for parallel operations.

#### Step 2: Check Hardware Configuration

Check your system parameters (CPU, RAM, GPU):

```bash
apt update
apt install neofetch
neofetch
```

Verify CUDA:

```bash
nvidia-smi
```

You should see information about your GPU, memory usage, and CUDA version.

> 💡 **TIP:** Note that "cpu-xx"  does not have any usefull GPU""

#### Step 3: Install Ollama

Open webpage https://ollama.com/download and check installation for your OS. For linux or for lab's "cpu-xx"""  run the automatic installation script for linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

If installation fails due to missing components (e.g., zstd):

```bash
apt update && apt install zstd
```

> ⚠️ **WARNING:** The installation file is about 1 GB - it may take some time.

#### Step 4: Start the Ollama Server

In a separate terminal, start the Ollama server (and keep it running):

```bash
ollama serve
```

In a second terminal, verify the version (and also if ollama is running):

```bash
ollama --version
```

Also check ollama parametres - try "ollama --help"

#### Step 5: Download and Run the Smallest Model

Download and run the smallest available model (qwen3:0.6b - about 0.5 GB - Alibaba cloud):

```bash
ollama run qwen2.5:0.5b
```

- Try interactive chat - ask something like "Who was JFK?"
- Exit chat with the `/exit` command
- Run it again - this time the model is not downloaded (it's already local)

#### Step 6: Download a Larger Model

Download the more powerful phi4-mini:3.8b model (about 2.5 GB - Microsoft):

You can also check all models at "https://ollama.com/library"

```bash
ollama pull phi4-mini:3.8b"
```

List all downloaded models:

```bash
ollama list
```

#### Step 7: Compare Models

Run the larger model:

```bash
ollama run phi4-mini:3.8b
```

Ask the same question as with the smaller model and compare:

- Quality of the response
- Generation speed (tokens/s)
- GPU/CPU usage (`nvidia-smi` in another terminal)

In another terminal, check running models:

```bash
ollama ps
```

Run a non-interactive query and measure a time:

```bash
ollama run phi4-mini:3.8b "Explain me what is Docker"
time ollama run phi4-mini:3.8b "Explain me what is Docker"
```

#### Step 8: Test the REST API

Verify that the Ollama API is running:

```bash
curl http://localhost:11434
```

You should receive the response "Ollama is running".

Try generation via API:

```bash
curl http://localhost:11434/api/generate -d '{"model": "qwen2.5:0.5b", "prompt": "Why is the sky blue?", "stream": false}'
```

> 💡 **TIP:** The `stream: false` parameter returns the entire response at once. With `stream: true` you get a chunked response.

#### Step 9: What Can My Hardware Run?

Install llmfit to analyze which models your hardware can handle:

```bash
curl -fsSL https://llmfit.axjns.dev/install.sh | sh
llmfit
```

The tool will recommend suitable models based on available RAM/VRAM.

---

## Lab B - Ollama and Open-WebUI

### Objective

Learn how to use the Open-WebUI web interface for more convenient interaction with local LLM models.

### Setup

For this lab, we use a pre-configured environment with the template `thelocallab/ollama-openwebui` on runpod.io, where Ollama and Open-WebUI are already installed and exposed to the internet. URL's are in student-xx.txt file

- Ollama API
- Open-WebUI

### Exercise 1 - Working with Open-WebUI

#### Step 1: Verify the Environment

Login to shell and check running Ollama and pre-installed models (should be qwen2.5-coder:1.5b). Also check CUDA

```bash
ollama list
ollama ps
nvidia-smi
```

#### Step 2: Test Ollama API via Proxy

Open the Ollama URL in your browser (replace XX with your number):

```
https://cewl9xarbXX-11434.proxy.runpod.net/
```

You should see "Ollama is running".

#### Step 3: Open Open-WebUI

Open Open-WebUI in your browser:

```
https://cewl9xarbXX-8080.proxy.runpod.net/
```

- Check which model is currently selected
- Try a chat with the pre-installed model

#### Step 4: Download Another Model

In the terminal, download llama3:

```bash
ollama pull llama3.2:3b
```

In Open-WebUI:

1. Open a new chat
2. Switch to the llama3 model (dropdown at the top)
3. Try the question "Tell me the history of Docker"

#### Step 5: Advanced Open-WebUI Features

- Dictate mode - voice input
- Voice mode - voice conversation
- Document upload - RAG functionality
- Create custom prompts and templates
- Admin panel (click on user left-bottom))

> ⚠️ **WARNING:** Public URL without authentication means anyone with the URL can use your Ollama instance! Always add authentication in production.

---

## Lab C - VS Code Integration (BONUS)

### Objective

Connect local Ollama as an AI assistant directly into VS Code.

### Exercise 1 - Continue.dev

#### Step 1: Download a Specialized Coding Model

```bash
ollama pull qwen2.5-coder:7b
```

#### Step 2: Install Continue.dev

- Open VS Code
- Extensions (Ctrl+Shift+X)
- Search for "Continue" and install

#### Step 3: Configuration

Open the config file (`~/.continue/config.json`) and add:

```json
{
  "models": [
    {
      "title": "Qwen Coder",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b",
      "apiBase": "http://localhost:11434"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Qwen Coder",
    "provider": "ollama",
    "model": "qwen2.5-coder:7b",
    "apiBase": "http://localhost:11434"
  }
}
```

#### Step 4: Usage

- `Ctrl/Cmd + L` - opens chat panel
- `Ctrl/Cmd + I` - inline edit
- Tab autocomplete works automatically

### Exercise 2 - Cline (Agentic Coding)

For advanced use, install the "Cline" extension:

- Can read and edit files
- Executes terminal commands
- Creates new files autonomously
- Similar to Claude Code, but with a local model

---

## Model Comparison

Use this table to select a suitable model based on your hardware:

| Model              | Size   | RAM/VRAM | Use Case            | Speed     |
| ------------------ | ------ | -------- | ------------------- | --------- |
| qwen3:0.6b         | 0.5 GB | 1-2 GB   | Testing, simple Q&A | Very fast |
| qwen2.5-coder:1.5b | 1 GB   | 2-3 GB   | Basic coding        | Very fast |
| qwen2.5-coder:3b   | 2 GB   | 4-5 GB   | Better coding       | Fast      |
| qwen2.5-coder:7b   | 4.7 GB | 8 GB     | Advanced coding     | Medium    |
| llama3.1:8b        | 5 GB   | 8 GB     | General purpose     | Medium    |
| llama3:70b         | 40 GB  | 48+ GB   | Highest quality     | Slow      |

---

## Troubleshooting

### Ollama Is Not Running

```bash
sudo systemctl status ollama
sudo systemctl restart ollama
```

Or manually:

```bash
ollama serve
```

### Model Is Slow

- Check that it runs on GPU: `nvidia-smi`
- Consider a smaller model

### Out of Memory Error

- Stop running models: `ollama stop <model>`
- Use a smaller model or quantized version (q4, q5)
- Restart Ollama: `ollama serve`

### Open-WebUI Does Not See Models

- Check the Ollama API URL in Open-WebUI Settings
- It should be `http://localhost:11434` or the proxy URL

---

## Useful Links

- Ollama documentation: https://ollama.com/docs
- Open-WebUI documentation: https://docs.openwebui.com/
- Continue.dev: https://docs.continue.dev/
- Qwen models: https://ollama.com/library/qwen2.5-coder
- Llama models: https://ollama.com/library/llama3.1

---

**Good luck with local LLMs! 🚀**
