{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNKdFL/CC1z0U3M9pCGTM9r",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rajitha123java/jira-data-engine/blob/AIBasics/GeminiAPI.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Jira Data Hygine -POC"
      ],
      "metadata": {
        "id": "R8PtB0SI-8YB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "\n",
        "# Public API endpoint\n",
        "url = \"https://api.gemini.com/v1/pubticker/btcusd\"\n",
        "\n",
        "# Make a GET request\n",
        "response = requests.get(url)\n",
        "\n",
        "# Parse and display the response\n",
        "if response.status_code == 200:\n",
        "    data = response.json()\n",
        "    print(data)\n",
        "else:\n",
        "    print(\"Error:\", response.status_code, response.text)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HiASZmIL_CtP",
        "outputId": "77e227ca-408e-471a-f29f-c89c99004947"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'bid': '107112.03', 'ask': '107121.98', 'last': '107127.61', 'volume': {'BTC': '525.95547278', 'USD': '56344352.7653414558', 'timestamp': 1751341574000}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pbftqago-jq1",
        "outputId": "9447165c-4426-49f5-8559-b063396c626f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "AI learns from data to make predictions or decisions.\n",
            "\n"
          ]
        }
      ],
      "source": [
        "\n",
        "\n",
        "from google import genai\n",
        "\n",
        "client = genai.Client(api_key=\"****\")\n",
        "\n",
        "response = client.models.generate_content(\n",
        "    model=\"gemini-2.0-flash\", contents=\"Explain how AI works in a few words\"\n",
        ")\n",
        "print(response.text)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "HvC1wM1N-03Q"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Mo9N5KmU-zve"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}