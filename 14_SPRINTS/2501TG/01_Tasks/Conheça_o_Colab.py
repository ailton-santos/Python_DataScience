{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "#avaliaçoes de produtos 1-5 estrelas"
      ],
      "metadata": {
        "id": "0RVk5d9QQ1xV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import statistics as st\n",
        "import random as ran"
      ],
      "metadata": {
        "id": "EVSZm-XeN2IO"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "avaliacoes = [ran.randint(1, 5) for i in range(50)]\n",
        "print(avaliacoes)"
      ],
      "metadata": {
        "id": "2xA3tSDFP8A6",
        "outputId": "9424ca33-3800-4eee-faa2-5c575a96ebe7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[5, 1, 5, 5, 1, 2, 2, 1, 2, 3, 2, 2, 5, 4, 5, 3, 5, 4, 5, 3, 4, 5, 5, 4, 1, 4, 3, 4, 4, 3, 4, 2, 3, 5, 1, 1, 2, 2, 1, 1, 1, 4, 2, 5, 5, 5, 5, 4, 4, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "moda_das_avaliacoes = st.mode(avaliacoes)\n",
        "print('\\nModa das avaliaçoes:', moda_das_avaliacoes)"
      ],
      "metadata": {
        "id": "ftdQOGS1P8Fd",
        "outputId": "6681dc2e-aeb8-4d91-dd05-33311b70556c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Moda das avaliaçoes: 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "desvio = st.stdev(avaliacoes)\n",
        "print('Desvio das avaliações:', desvio)"
      ],
      "metadata": {
        "id": "eNS9a79vP8JG",
        "outputId": "6b7cbf0c-7471-48d7-f3b8-d7d4994d24a1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Desvio das avaliações: 1.4957081457098698\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "media = st.mean(avaliacoes)\n",
        "mediana = st.median(avaliacoes)\n",
        "print('Média:', media)\n",
        "print('Mediana:', mediana)"
      ],
      "metadata": {
        "id": "QO0oXHSnQtpG",
        "outputId": "7974bb0e-7145-42d2-ce42-6a0099b093c2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Média: 3.26\n",
            "Mediana: 4.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if media <= 2:\n",
        "    print('A avaliação média é ruim')\n",
        "elif media > 2 and media < 4:\n",
        "    print('A avaliação média é mediana')\n",
        "elif media >= 4:\n",
        "    print('A avaliação média é boa')"
      ],
      "metadata": {
        "id": "3rU5oFgqQt0_",
        "outputId": "916d319f-a036-4ec8-efe9-f2e5b54da37e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A avaliação média é mediana\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Conheça o Colab",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}