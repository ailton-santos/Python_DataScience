{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "WZZtGVaPiz4f"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "# Criação de listas vazias para armazenar dados\n",
        "nomes = []#Criando uma variável do tipo Lista vazia para receber os dados de nomes\n",
        "idades = []\n",
        "alturas = []\n",
        "pesos = []\n",
        "\n",
        "# Abrir e ler o arquivo CSV\n",
        "with open('dados1.csv', 'r', encoding = 'ISO-8859-1') as batata:#\n",
        "    lines = batata.readlines()\n",
        "\n",
        "\n",
        "    for line in lines[1:]:  # Ignorar o cabeçalho\n",
        "        nome, idade, altura, peso = line.strip().split(',')\n",
        "        nomes.append(nome)\n",
        "        idades.append(int(idade))\n",
        "        alturas.append(int(altura))\n",
        "        pesos.append(float(peso))\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "nomes_nd = np.array(nomes)\n",
        "idades_nd = np.array(idades)\n",
        "alturas_nd = np.array(alturas)\n",
        "pesos_nd = np.array(pesos)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 1)\tQual é a média das idades das pessoas na base de dados?"
      ],
      "metadata": {
        "id": "PIkuMbbpFaG4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "media_idades = np.mean(idades_nd)\n",
        "print(f'{media_idades:.2f}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YzVtEZ77lNTk",
        "outputId": "77208aa4-a352-4679-818d-c78519e44b51"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "41.58\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 2)\tQual é a altura máxima registrada entre as pessoas?"
      ],
      "metadata": {
        "id": "1yL6v3gPFfNl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "altura_maxima = np.max(alturas_nd)\n",
        "print(altura_maxima)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fq4uHj_VlZaw",
        "outputId": "32f56b26-8980-4efb-ae63-94f3b2068919"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "190\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 3)\tQuantas pessoas possuem peso acima de 70 kg?"
      ],
      "metadata": {
        "id": "y5b0n7NZFhuv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pesos_70 = np.where(pesos_nd > 70)\n",
        "\n",
        "print(len(nomes_nd[pesos_70]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BZFmIKi_lrHW",
        "outputId": "af00d059-ee96-4be8-e979-904a913fde87"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "178\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pesos_70 = np.count_nonzero(pesos_nd > 70)\n",
        "print(pesos_70)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jPhGC4DOmSgW",
        "outputId": "fd677afa-5512-4595-bb06-5bc41bef505d"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "178\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 4)\tQual é o desvio padrão das idades das pessoas?"
      ],
      "metadata": {
        "id": "oOVKFvDPFka_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "desvio_idades = np.std(idades_nd)\n",
        "print(round(desvio_idades,2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fX_ra0EyoLjz",
        "outputId": "ebff2303-281b-4fb2-ebd1-7f699ef13708"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "13.77\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 5:)\tQuem é a pessoa mais velha na base de dados?"
      ],
      "metadata": {
        "id": "odeHSsgAFmvf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "idade_maxima = np.max(idades_nd)\n",
        "print(idade_maxima)\n",
        "\n",
        "pessoas_65 = np.count_nonzero(idades_nd == idade_maxima)\n",
        "print(pessoas_65)\n",
        "\n",
        "nomes_pessoas_65 = nomes_nd[np.where(idades_nd == idade_maxima)]\n",
        "print(nomes_pessoas_65)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qO35g7TnoXT4",
        "outputId": "95fbb699-c909-40fa-e7ab-de9aff42ea9c"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "65\n",
            "6\n",
            "['Lúcia' 'Carlos' 'Sofia' 'Rafael' 'Pedro' 'Laura']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 6)\tQual é o Índice de Massa Corporal (IMC) médio das pessoas?"
      ],
      "metadata": {
        "id": "DLy3up2mFs86"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "imc_nd = np.array([pesos_nd[i] /\n",
        "                   ((alturas_nd[i]/100)**2) for i in range(len(nomes_nd))])\n",
        "imc_nd"
      ],
      "metadata": {
        "id": "lCSyuX13pmuo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "imc_nd = np.array([pesos_nd / ((alturas_nd/100)**2)])\n",
        "imc_nd\n",
        "\n",
        "# def calcula_imc(peso,altura):\n",
        "#   imc_1 = np.array([peso / ((altura/100)**2)])\n",
        "#   return imc_1\n",
        "\n",
        "# imc_aluno = calcula_imc(80,170)\n",
        "# imc_aluno"
      ],
      "metadata": {
        "id": "qoxImgXeq8sN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "imc = []\n",
        "\n",
        "for i in range(len(nomes_nd)):\n",
        "\n",
        "    resultado = pesos_nd[i] /((alturas_nd[i]/100)**2)\n",
        "    imc.append(resultado)\n",
        "\n",
        "print(imc)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ja4ZFQ-krF_m",
        "outputId": "2de93087-7c3f-40ef-d4bb-32502bcfd2c6"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[19.304498269896197, 24.895119939761198, 21.85240185950413, 24.64301253906095, 25.511555384681106, 23.989619377162633, 28.884866265097845, 30.433238636363637, 35.547081017485496, 20.980609418282548, 26.41923921840675, 25.470279661866417, 25.974398508372477, 35.97167833550888, 19.986419194205524, 20.874999999999996, 24.08227709310995, 15.877558099202219, 17.63108535595308, 28.740091077753416, 18.090199042579997, 38.79296874999999, 33.780329820384445, 26.620702863161927, 29.695312499999993, 26.07173046733486, 23.39061689203626, 23.04518506649575, 27.90942293644996, 23.866066583676464, 35.78538169080268, 19.10148865784499, 25.176253805479888, 24.37524029219531, 25.06492382271468, 25.366312102182924, 18.733969426490205, 39.717556247533004, 23.002659266967274, 24.453333333333333, 28.966023875114786, 19.50543232231779, 18.736270089027627, 36.491516620498615, 18.659686614794364, 25.24447278911565, 29.077122389879587, 27.334330453893347, 26.36933928404232, 19.887258849480062, 16.518005540166207, 21.038931643277504, 27.196493791088383, 36.629154277541495, 30.468776103444817, 24.71831210699352, 18.173239154679855, 22.080195534416696, 26.03944485025566, 36.28906249999999, 31.731064426998813, 25.212121212121215, 14.593707559981892, 34.653333333333336, 23.82067291016302, 18.36462501282446, 31.06222222222222, 22.081165452653483, 15.998611286453729, 20.60774287801315, 34.8057559507735, 29.498269896193776, 27.80715850986121, 27.65051903114187, 26.61981426368819, 29.17823934307451, 20.12974170325541, 20.422160633800846, 18.762913223140497, 27.611078043485875, 33.0235539176414, 25.831425598335066, 26.42658783481143, 16.169753086419753, 17.833295608872795, 26.166706049149337, 27.78190914007572, 23.476365373704798, 30.756289056240984, 24.287480370209494, 24.785342653771266, 18.16110608283137, 14.969529085872576, 27.220878497417058, 27.770711810885487, 17.431469629271827, 28.943717796274274, 23.186252095717112, 37.84044559449147, 21.54847645429363, 21.68114616674287, 21.07716049382716, 34.08107192592872, 21.97887811634349, 37.01293872694825, 26.004182141631034, 21.487153433009148, 21.854938271604937, 25.72683042601163, 27.946502205170496, 33.75941230486685, 28.089506172839506, 27.60359817832813, 28.035875961973748, 28.6953981008035, 29.759329367225533, 26.768023167200116, 32.312804082117, 19.16699696128947, 28.23348591666945, 28.617810760667908, 26.8719723183391, 19.684356573014217, 21.816847010756803, 21.624935722479332, 21.691235378945677, 43.14723038463225, 22.37135633551458, 18.727365323675873, 19.8808864265928, 25.780864197530864, 24.129624750649253, 30.110408057851238, 31.365989142785, 27.068443556692987, 17.40467820443483, 25.085872576177287, 33.444328824141515, 19.790903128737312, 29.84816326530612, 24.81539643823716, 17.270204081632652, 21.226339812952855, 28.18533934558908, 30.387511478420574, 26.811788945623935, 23.27440926530173, 38.414151925078045, 28.762843915841774, 33.1007831469512, 17.160835812728706, 26.185595567867036, 32.148788927335644, 21.86842193190551, 26.506939371804233, 26.20795975495963, 34.38281249999999, 36.125149492689324, 26.520381328073636, 24.640926871510043, 16.55104636374147, 29.87328034728207, 22.70084252996321, 30.561166519378865, 24.18116585008294, 25.286511410337802, 22.001219326322204, 15.997680168493025, 23.147506925207754, 24.204249601075, 34.26165519056182, 20.426592797783933, 23.85674931129477, 21.206790123456788, 33.48098767597912, 21.580537834620433, 20.87561404137832, 30.896193771626304, 29.408626733729612, 29.391020408163268, 23.549891833423477, 16.969529085872576, 25.35430839002268, 33.01146045641351, 33.72406813965256, 23.426887094707165, 33.45028726810227, 16.677187223835375, 22.048251721931575, 19.881862209904536, 26.778546712802772, 25.25057360222195, 20.55491401641647, 18.960082394432135, 14.202216066481995, 33.336753189015425, 19.277175890932504, 31.61064842355741, 21.793588607051955, 23.39591836734694, 26.810515873015877, 23.8005540166205, 22.9275060700659, 32.345186587344514, 24.008963514707737, 29.02579714789296, 22.08404195011338, 19.62143503847895, 22.177021696252464, 26.185673035085635, 27.06824354911725, 30.28326122228232, 22.011718749999996, 24.773242630385493, 28.65071106486299, 20.55609225938896, 22.923292637050718, 34.10156249999999, 18.48850723140496, 18.518652924952825, 38.95510273826306, 30.187499999999993, 19.808999081726355, 24.73118279569892, 18.44034879112168, 30.588235294117652, 33.17906336088154, 32.30251562249639, 38.04103185595568, 34.22785953554895, 21.72363060208239, 21.718454631379963, 33.12757995447706, 20.9963580473788, 30.84967757024959, 28.334711720226842, 21.647058823529417, 28.02947239156177, 34.97550248832992, 28.64928824984761, 41.408414127423825, 26.91246915372333, 30.130145750756846, 21.222486615110057, 19.990740740740737, 25.211447832464657, 20.34729638859222, 25.87534626038781, 40.53843490304709, 34.391784003483814, 26.87543252595156, 28.73453578448375, 31.043615703361954, 36.11191754971694, 32.3048668503214, 22.700617283950614, 19.70736168267032, 20.800315536591487, 19.272976680384083, 22.35276621058894, 27.29176097781802, 34.6593204775023, 32.943469785575054, 23.95634711347316, 26.99251298152397, 34.43523242630386, 32.07967458677686, 31.886734379809173, 35.05020775623269, 25.766385823345594, 27.85948743845474, 24.70825115055884, 29.782031155657528, 22.275069361870788, 28.26973062381852, 17.304111596105123, 15.532544378698224, 27.316543777330907, 27.197802197802197, 26.96069944598338, 19.251901944209635, 32.708907254361804, 17.90740740740741, 26.998163099662523, 28.18878890795141, 20.27777777777778, 23.257751852988903, 21.071848756541847, 28.22222222222222, 20.631117604090576, 27.81061224489796, 38.783848742188745, 19.73062381852552, 21.50415512465374, 20.254847645429365, 29.883586654598794, 35.69146005509642, 23.569141704311214, 27.301086449854783, 16.003086419753085]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 7)\tQual é a diferença de idade entre a pessoa mais nova e a mais velha?"
      ],
      "metadata": {
        "id": "UWE5QXliFwr1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "idade_minima = np.min(idades_nd)\n",
        "print(idade_minima)\n",
        "print(idade_maxima)\n",
        "diferenca = idade_maxima-idade_minima\n",
        "print(diferenca)\n",
        "\n",
        "\n",
        "diferenca_2 = np.ptp(idades)\n",
        "print(diferenca_2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "15VDuHpBsLcJ",
        "outputId": "12f4f39f-65d6-40d4-db2c-59aeddedb1a4"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "18\n",
            "65\n",
            "47\n",
            "47\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 8)\tQuem é a pessoa mais alta na base de dados?"
      ],
      "metadata": {
        "id": "ATuqU6unGIrU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "alturas_190 = np.count_nonzero(alturas_nd == altura_maxima)\n",
        "print(alturas_190)\n",
        "pessoas_190 = nomes_nd[np.where(alturas_nd == altura_maxima)]\n",
        "print(pessoas_190)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WS1rvg4DtHZs",
        "outputId": "878cc4d5-4e39-4475-d965-a29ef26d8a4a"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "14\n",
            "['Carlos' 'Lúcia' 'Miguel' 'Laura' 'Carlos' 'Sofia' 'Sofia' 'João'\n",
            " 'Carlos' 'Rafael' 'Rafael' 'Lúcia' 'Carlos' 'Carlos']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 9)\tQual é a altura média das pessoas com idade entre 25 e 30 anos?"
      ],
      "metadata": {
        "id": "-krYRXWqGNlr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "idades_25_30 = np.where(np.logical_and(idades_nd >= 25, idades_nd <= 30))\n",
        "media_alturas_25_30 = np.mean(alturas_nd[idades_25_30])\n",
        "print(round(media_alturas_25_30,2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FZTnM1WuuNWd",
        "outputId": "7b341ef5-9e75-446e-83f2-3d74253c76bf"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "171.69\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 10)\tQuantas pessoas têm IMC acima de 25 (indicando sobrepeso)?"
      ],
      "metadata": {
        "id": "OvzfRa6LGSMq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "imc_25 = np.count_nonzero(imc_nd >=25)\n",
        "imc_25"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HyOSNx-DvpiP",
        "outputId": "178da4f7-4b33-4d6b-935f-70677b6da8fe"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "162"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 11)\tQuais são os nomes das pessoas com altura acima de 170 cm?"
      ],
      "metadata": {
        "id": "TD6fE3ZeGYbS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "alturas_170 = np.where(alturas_nd >170)\n",
        "nomes_nd[alturas_170]"
      ],
      "metadata": {
        "id": "Ah9P8cEQGU4q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 12)\tQual é a idade média das pessoas com peso abaixo de 70 kg?"
      ],
      "metadata": {
        "id": "O15lpqxSIuyh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pesos_abaixo_70 = np.where(pesos_nd < 70)\n",
        "media_abaixo_70 = (idades_nd[pesos_abaixo_70]).mean()\n",
        "media_abaixo_70\n",
        "\n",
        "media_abaixo_70 = np.mean(idades_nd[pesos_abaixo_70])\n",
        "media_abaixo_70"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eIsTTi6kIhF7",
        "outputId": "4cbb3154-e8f6-4b53-8bf1-b6bdd72b9a32"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "41.64754098360656"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 13)\tQuantas pessoas têm idade ímpar na base de dados?"
      ],
      "metadata": {
        "id": "OvylnNyqKQ2H"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "idade_impar = np.count_nonzero((idades_nd % 2) != 0)\n",
        "idade_impar\n",
        "\n",
        "# idade_impar_index = np.where((idades_nd % 2) != 0)\n",
        "# nomes_nd[idade_impar_index]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "48zsI_6tJBhl",
        "outputId": "c3c3dbba-3324-43d2-f155-b399f1f6c024"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "149"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 14)\tQuem é a pessoa cuja altura está mais próxima da média (175 cm)?"
      ],
      "metadata": {
        "id": "GXxhp1uUMa5R"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "diferenca = np.abs(alturas_nd - 175)\n",
        "diferenca\n",
        "\n",
        "menor_diferenca = np.min(diferenca)\n",
        "menor_diferenca\n",
        "\n",
        "indices_mais_proximos = np.count_nonzero(diferenca == menor_diferenca)\n",
        "indices_mais_proximos\n",
        "\n",
        "indices_mais_proximos = np.where(diferenca == menor_diferenca)\n",
        "indices_mais_proximos\n",
        "\n",
        "valores_mais_proximos = alturas_nd[indices_mais_proximos]\n",
        "valores_mais_proximos\n",
        "\n",
        "pessoas_175 = nomes_nd[indices_mais_proximos]\n",
        "pessoas_175"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PRcXQR7kMeZA",
        "outputId": "a7924f84-4604-4699-b4cf-3d541c8034b8"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Lúcia', 'Pedro', 'Miguel', 'Sofia', 'Ana'], dtype='<U6')"
            ]
          },
          "metadata": {},
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#  Diferença entre np.argmin( ) e np.min( )\n",
        "  argmin( ) retorna a posição\n",
        "\n",
        "  \n",
        "  min( ) retorna o valor"
      ],
      "metadata": {
        "id": "s8PAetHtWVlR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "arg_min = np.argmin(pesos_nd)\n",
        "min = np.min(pesos_nd)\n",
        "print(arg_min)\n",
        "print(min)\n",
        "print(pesos_nd[arg_min])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KY-DBdppVli7",
        "outputId": "c7ff8cdd-720e-4d50-976b-4dfe6c002aaf"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "150\n",
            "50.18\n",
            "50.18\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 15)\tCalcule e liste os IMCs de todas as pessoas na base de dados."
      ],
      "metadata": {
        "id": "c7IGMcL0WuUT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "imc_nd"
      ],
      "metadata": {
        "id": "56XbOCevWtTt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 16)\tQuem é a pessoa mais pesada na base de dados?"
      ],
      "metadata": {
        "id": "Qph2mUSvW4JK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "maior_peso = np.max(pesos_nd)\n",
        "maior_peso\n",
        "\n",
        "maior_peso_pos = np.argmax(pesos_nd)\n",
        "print(maior_peso_pos)\n",
        "\n",
        "pesssoas_encorpadas = np.where(pesos_nd == maior_peso )\n",
        "print(nomes_nd[pesssoas_encorpadas])\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sxTn9T6rW3lk",
        "outputId": "ceda5307-8a73-4a1f-a39f-3a8a04d9589f"
      },
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "104\n",
            "['João']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 17)\tQuais pessoas estão com sobrepeso (IMC > 25)?"
      ],
      "metadata": {
        "id": "8Pwq0hRZaFxr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "imc_25_nomes = np.where(imc_nd > 25)\n",
        "imc_25_nomes = imc_25_nomes[1]\n",
        "imc_25_nomes = nomes_nd[imc_25_nomes]\n",
        "imc_25_nomes"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aK_0E77JXtOn",
        "outputId": "81291081-7d28-46c6-9923-fa21d30781ca"
      },
      "execution_count": 82,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['João', 'Ana', 'Carlos', 'Ana', 'Ana', 'Miguel', 'Lúcia', 'Maria',\n",
              "       'Rafael', 'João', 'Rafael', 'Carlos', 'Laura', 'Lúcia', 'João',\n",
              "       'Sofia', 'Miguel', 'Pedro', 'Lúcia', 'Rafael', 'Maria', 'Rafael',\n",
              "       'João', 'Lúcia', 'Miguel', 'Lúcia', 'Miguel', 'Rafael', 'Rafael',\n",
              "       'Ana', 'João', 'Ana', 'Pedro', 'Laura', 'Sofia', 'Laura', 'Rafael',\n",
              "       'Carlos', 'Pedro', 'Miguel', 'Carlos', 'João', 'Miguel', 'Ana',\n",
              "       'Carlos', 'Pedro', 'João', 'Lúcia', 'Rafael', 'Ana', 'Miguel',\n",
              "       'Rafael', 'Miguel', 'João', 'Rafael', 'João', 'Pedro', 'Carlos',\n",
              "       'Miguel', 'Maria', 'Ana', 'Rafael', 'Carlos', 'Lúcia', 'Rafael',\n",
              "       'Sofia', 'Pedro', 'João', 'Rafael', 'Ana', 'Maria', 'Sofia',\n",
              "       'Sofia', 'Sofia', 'Laura', 'Lúcia', 'Sofia', 'Rafael', 'Sofia',\n",
              "       'Maria', 'Miguel', 'Carlos', 'Sofia', 'Carlos', 'Carlos', 'Miguel',\n",
              "       'Lúcia', 'Rafael', 'Rafael', 'Rafael', 'Laura', 'Pedro', 'Rafael',\n",
              "       'Ana', 'Laura', 'Maria', 'Miguel', 'Miguel', 'Sofia', 'João',\n",
              "       'Ana', 'Lúcia', 'Pedro', 'Laura', 'Lúcia', 'Pedro', 'Carlos',\n",
              "       'Sofia', 'Carlos', 'Rafael', 'Maria', 'Miguel', 'Rafael', 'Rafael',\n",
              "       'Lúcia', 'Rafael', 'João', 'João', 'Ana', 'Carlos', 'Laura',\n",
              "       'João', 'João', 'Rafael', 'Sofia', 'Laura', 'Maria', 'Sofia',\n",
              "       'Maria', 'Laura', 'Lúcia', 'Laura', 'Pedro', 'Lúcia', 'Lúcia',\n",
              "       'Ana', 'Ana', 'Lúcia', 'Lúcia', 'Miguel', 'Maria', 'Maria',\n",
              "       'Miguel', 'Miguel', 'Laura', 'Pedro', 'Maria', 'Carlos', 'João',\n",
              "       'Maria', 'Carlos', 'Maria', 'Lúcia', 'Maria', 'Sofia', 'Pedro',\n",
              "       'Pedro', 'Ana', 'Miguel', 'Laura', 'Maria', 'Ana'], dtype='<U6')"
            ]
          },
          "metadata": {},
          "execution_count": 82
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 18)\tQual é a média das idades das pessoas que têm mais de 170 cm de altura?"
      ],
      "metadata": {
        "id": "PukdxByca4sB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pessoas_170 = np.where(alturas_nd > 170)\n",
        "idades_pessoas_170 = idades_nd[pessoas_170]\n",
        "round(idades_pessoas_170.mean(),2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QPF9OTIea9Aa",
        "outputId": "c168cc42-c2e6-4533-bfd6-a7aebb6a500f"
      },
      "execution_count": 87,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "42.41"
            ]
          },
          "metadata": {},
          "execution_count": 87
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 19)\tQuantas pessoas têm idade entre 25 e 30 anos e altura abaixo de 170 cm?"
      ],
      "metadata": {
        "id": "BNYQhjKqbdwa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pessoas_25_30 = np.count_nonzero(np.logical_and(idades_nd >= 25,idades_nd <=30, alturas_nd < 170))\n",
        "pessoas_25_30"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mrnsMFQnbcO5",
        "outputId": "cdf6b982-83ac-46e5-ec54-7e7b9574ffc2"
      },
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "36"
            ]
          },
          "metadata": {},
          "execution_count": 89
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 20)\tQuem é a pessoa mais leve na base de dados?"
      ],
      "metadata": {
        "id": "WdES6zdLctEz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "peso_leve = np.min(pesos_nd)\n",
        "peso_leve\n",
        "\n",
        "pesos_leve = np.count_nonzero(pesos_nd == peso_leve)\n",
        "pesos_leve\n",
        "\n",
        "peso_leve_pos = np.argmin(pesos_nd)\n",
        "peso_leve_pos\n",
        "\n",
        "nomes_nd[peso_leve_pos]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "tQSWfTD9cwBY",
        "outputId": "fc43fb3e-43ad-4431-fae5-c5688c4df329"
      },
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Sofia'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 95
        }
      ]
    }
  ]
}