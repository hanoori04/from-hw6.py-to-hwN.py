{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMl+fa9fdwwI92tOiZx9ZvY",
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
        "<a href=\"https://colab.research.google.com/github/hanoori04/from-hw6.py-to-hwN.py/blob/main/hw10.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z3_IaaMnp594",
        "outputId": "0ed10cc0-1f74-46dd-ea3f-badfb49d2a18"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "개인점수: 30.0 20.0 10.0 \n",
            "평균: 20.0\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "import pickle\n",
        "\n",
        "def input_scores():\n",
        "    scores = []\n",
        "\n",
        "    i = 1\n",
        "    while True:\n",
        "        score = float(input(f\"#{i}? \"))\n",
        "        i += 1\n",
        "        if score < 0:\n",
        "            break\n",
        "        scores.append(score)\n",
        "    return scores\n",
        "\n",
        "\n",
        "def get_average(scores):\n",
        "    if len(scores) == 0:\n",
        "        return 0\n",
        "    average = sum(scores) / len(scores)\n",
        "    return average\n",
        "\n",
        "\n",
        "def show_scores(scores, average):\n",
        "    print(\"개인점수:\", end=' ')\n",
        "    for score in scores:\n",
        "        print(score, end=' ')\n",
        "    print()\n",
        "\n",
        "    if average != 0:\n",
        "        print(\"평균:\", format(average, \".1f\"))\n",
        "\n",
        "\n",
        "def save_scores(scores, file_path):\n",
        "    with open(file_path, \"wb\") as file:\n",
        "        pickle.dump(scores, file)\n",
        "\n",
        "\n",
        "def load_scores(file_path):\n",
        "    if os.path.exists(file_path):\n",
        "        with open(file_path, \"rb\") as file:\n",
        "            scores = pickle.load(file)\n",
        "        return scores\n",
        "    return []\n",
        "\n",
        "\n",
        "file_path = \"score.bin\"\n",
        "\n",
        "\n",
        "loaded_scores = load_scores(file_path)\n",
        "show_scores(loaded_scores, get_average(loaded_scores))\n",
        "\n",
        "\n",
        "if not os.path.exists(file_path):\n",
        "    scores_list = input_scores()\n",
        "    save_scores(scores_list, file_path)\n",
        "\n",
        "    \n",
        "    average_score = get_average(scores_list)\n",
        "    show_scores(scores_list, average_score)"
      ]
    }
  ]
}