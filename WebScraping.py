{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "url='https://www.python.org/'\n",
    "r=requests.get(url)\n",
    "soup=BeautifulSoup(r.content,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"small-widget get-started-widget\">\n",
       "<h2 class=\"widget-title\"><span aria-hidden=\"true\" class=\"icon-get-started\"></span>Get Started</h2>\n",
       "<p>Whether you're new to programming or an experienced developer, it's easy to learn and use Python.</p>\n",
       "<p><a href=\"/about/gettingstarted/\">Start with our Beginner’s Guide</a></p>\n",
       "</div>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('div',class_='small-widget')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<h2 class=\"widget-title\"><span aria-hidden=\"true\" class=\"icon-get-started\"></span>Get Started</h2>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('div',class_='small-widget').h2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Get Started'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('div',class_='small-widget').h2.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<span aria-hidden=\"true\" class=\"icon-get-started\"></span>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('div',class_='small-widget').h2.next"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Whether you're new to programming or an experienced developer, it's easy to learn and use Python.\""
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('div',class_='small-widget').h2.next_sibling.next_sibling.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<div class=\"small-widget get-started-widget\">\n",
       " <h2 class=\"widget-title\"><span aria-hidden=\"true\" class=\"icon-get-started\"></span>Get Started</h2>\n",
       " <p>Whether you're new to programming or an experienced developer, it's easy to learn and use Python.</p>\n",
       " <p><a href=\"/about/gettingstarted/\">Start with our Beginner’s Guide</a></p>\n",
       " </div>,\n",
       " <div class=\"small-widget download-widget\">\n",
       " <h2 class=\"widget-title\"><span aria-hidden=\"true\" class=\"icon-download\"></span>Download</h2>\n",
       " <p>Python source code and installers are available for download for all versions!</p>\n",
       " <p>Latest: <a href=\"/downloads/release/python-397/\">Python 3.9.7</a></p>\n",
       " </div>,\n",
       " <div class=\"small-widget documentation-widget\">\n",
       " <h2 class=\"widget-title\"><span aria-hidden=\"true\" class=\"icon-documentation\"></span>Docs</h2>\n",
       " <p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>\n",
       " <p><a href=\"https://docs.python.org\">docs.python.org</a></p>\n",
       " </div>,\n",
       " <div class=\"small-widget jobs-widget last\">\n",
       " <h2 class=\"widget-title\"><span aria-hidden=\"true\" class=\"icon-jobs\"></span>Jobs</h2>\n",
       " <p>Looking for work or have a Python related position that you're trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>\n",
       " <p><a href=\"//jobs.python.org\">jobs.python.org</a></p>\n",
       " </div>]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find_all(class_='small-widget')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Get Started'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find_all(class_='small-widget')[0].h2.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "elementos = soup.find_all(class_='small-widget')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Get Started\n",
      "Download\n",
      "Docs\n",
      "Jobs\n"
     ]
    }
   ],
   "source": [
    "for elemento in elementos:\n",
    "  print(elemento.h2.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csv_file=open('fornecedores.csv','w',newline='')\n",
    "csv_writer=csv.writer(csv_file)\n",
    "csv_writer.writerow(['Id','empresa','telefone','site','email'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.abimad.com.br/associados.php'\n",
    "r=requests.get(url)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup=BeautifulSoup(r.content,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<figure class=\"col-xs-12 col-sm-6 col-md-4 section-sm-bottom-35 section-xs-0 wow fadeIn\" data-wow-delay=\".1s\">\n",
       "<a class=\"dropdown-toggle\" data-toggle=\"dropdown\" href=\"#\">\n",
       "<div class=\"relativer img-hover-container zindex-1\">\n",
       "<div class=\"bw-gradient absoluter pos-b-0 zindex-1\"></div>\n",
       "<img alt=\"\" class=\"zoom-hover\" src=\"/repositorio/timthumb.php?src=repositorio/empresas/m4u6q6.jpg&amp;h=240&amp;w=370&amp;zc=1\"/>\n",
       "<h5 class=\"f-800 mt-0 pt-0 text-white animated-border-bottom ml-30 absoluter pos-b-30 zindex-1 no-pointerevents truncate\">2A Cerâmica</h5>\n",
       "</div>\n",
       "</a>\n",
       "<figcaption class=\"dropdown-menu no-drawer-animation to-top dropdown-results col-xs-12 text-14 mt-0 pb-0 white-bg\">\n",
       "<div class=\"p-30 pb-10 mb-20\">\n",
       "<p class=\"ib mt-10\">\n",
       "<i class=\"col-xs-1 fa-user p-0 m-0 abimad-red text-24 text-center\"></i>\n",
       "<span class=\"col-xs-11\">André Terassi</span>\n",
       "</p>\n",
       "<p class=\"ib mt-10\">\n",
       "<i class=\"col-xs-1 fa-phone p-0 m-0 abimad-red text-24 text-center\"></i>\n",
       "<span class=\"col-xs-11\">+55 (19) 3581-3281</span>\n",
       "</p>\n",
       "<a class=\"ib mt-10\" href=\"http://www.2aceramica.com.br\">\n",
       "<p>\n",
       "<i class=\"col-xs-1 fa-link p-0 m-0 abimad-red text-24 text-center\"></i>\n",
       "<span class=\"col-xs-11\">www.2aceramica.com.br</span>\n",
       "</p>\n",
       "</a>\n",
       "<p class=\"ib mt-10\">\n",
       "<i class=\"col-xs-1 fa-at p-0 m-0 abimad-red text-24 text-center\"></i>\n",
       "<span class=\"col-xs-11\"><a href=\"mailto:contato@2aceramica.com.br\">contato@2aceramica.com.br </a></span>\n",
       "</p>\n",
       "<a class=\"ib mt-10\" href=\"https://www.instagram.com/2aceramica/\" target=\"_blank\">\n",
       "<p>\n",
       "<i class=\"col-xs-1 fa-instagram p-0 m-0 abimad-red text-24 text-center\"></i>\n",
       "<span class=\"col-xs-11\">@2aceramica/</span>\n",
       "</p>\n",
       "</a>\n",
       "</div>\n",
       "<a href=\"/associado/2a_ceramica\">\n",
       "<span class=\"abimad-red border border-3pt col-xs-10 col-xs-offset-1 f-800 mb-30 pb-10 pt-10 red text-center upper btn-href-transparent-to-red\">Ir para página do associado</span>\n",
       "</a>\n",
       "</figcaption>\n",
       "</figure>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('figure')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2A Cerâmica'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('figure').h5.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "empresa = soup.find('figure').h5.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2A Cerâmica'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "empresa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<span class=\"col-xs-11\">André Terassi</span>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('figure').span"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<span class=\"col-xs-11\">+55 (19) 3581-3281</span>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('figure').find('i',class_= 'fa-phone').next_element.next_element"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'+55 (19) 3581-3281'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('figure').find('i',class_= 'fa-phone').next_element.next_element.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "telefone = soup.find('figure').find('i',class_= 'fa-phone').next_element.next_element.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'www.2aceramica.com.br'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('figure').find('i',class_= 'fa-link').next_element.next_element.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "site = soup.find('figure').find('i',class_= 'fa-link').next_element.next_element.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'contato@2aceramica.com.br '"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find('figure').find('i',class_= 'fa-at').next_element.next_element.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "contato@2aceramica.com.br \n"
     ]
    }
   ],
   "source": [
    "email = soup.find('figure').find('i',class_= 'fa-at').next_element.next_element.text\n",
    "print(email)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "todos_elementos = soup.find_all('figure')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empresa: 2A Cerâmica\n",
      "Telefone:+55 (19) 3581-3281\n",
      "Site:www.2aceramica.com.br\n",
      "E-mail:contato@2aceramica.com.br \n",
      "----------------------------------------\n",
      "Empresa: 6F Decorações\n",
      "Telefone:+55 (11) 4612-3600\n",
      "Site:www.6f.com.br\n",
      "E-mail:marketing@6f.com.br \n",
      "----------------------------------------\n",
      "Empresa: Abdalla\n",
      "Telefone:+55 (11) 3328-6228\n",
      "Site:www.abdalla.com.br\n",
      "E-mail:comex@abdalla.com.br \n",
      "----------------------------------------\n",
      "Empresa: ACCORD Iluminação\n",
      "Telefone:+55 (46) 3581-5950\n",
      "Site:www.accordiluminacao.com.br\n",
      "E-mail:accord@accordiluminacao.com.br \n",
      "----------------------------------------\n",
      "Empresa: Adm Moveis e Design Eireli.\n",
      "Telefone:+55 (54) 3462-7245\n",
      "Site:www.admmoveis.com.br\n",
      "E-mail:vendas@admmoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Aluminas Móveis\n",
      "Telefone:+55 (37) 3381-3400\n",
      "Site:www.aluminas.com.br\n",
      "E-mail:wuander@aluminas.com.br \n",
      "----------------------------------------\n",
      "Empresa: Ana Verona - Ana Lucia Rodrigues Verona - ME\n",
      "Telefone:+55 (15) 3264-1279\n",
      "Site:www.anaverona.com.br\n",
      "E-mail:anaverona@anaverona.com.br \n",
      "----------------------------------------\n",
      "Empresa: Ancezki\n",
      "Telefone:+55 (54) 3453-3224\n",
      "Site:www.ancezki.com.br\n",
      "E-mail:comercial@ancezki.com.br \n",
      "----------------------------------------\n",
      "Empresa: Anfer Indústria e Comercio de Prod. para Dec. Ltda\n",
      "Telefone:+55 (48) 3651-1750\n",
      "Site:www.anferdesign.com.br\n",
      "E-mail:anferdesign@anferdesign.com.br \n",
      "----------------------------------------\n",
      "Empresa: Antica Comercio de Objetos e Artigos de Decoração Ltda.\n",
      "Telefone:+55 (11) 4521-0268\n",
      "Site:www.antica.com.br\n",
      "E-mail:marco@antica.com.br \n",
      "----------------------------------------\n",
      "Empresa: Armil - Móveis Armil Ltda.\n",
      "Telefone:+55 (54) 3286-8270 (54) 3286-8232\n",
      "Site:www.moveisarmil.com.br\n",
      "E-mail:comercial@moveisarmil.com.br \n",
      "----------------------------------------\n",
      "Empresa: Arte Nova Ind. e Com. de Móveis e Decoração Ltda.\n",
      "Telefone:+55 (43) 3325-4040\n",
      "Site:www.artenova.ind.br\n",
      "E-mail:comercial@artenova.com.br \n",
      "----------------------------------------\n",
      "Empresa: Artecouro Sofás\n",
      "Telefone:+55 (43) 3274-5640\n",
      "Site:www.artecourosofas.com.br\n",
      "E-mail:artecouro@artecourosofas.com.br \n",
      "----------------------------------------\n",
      "Empresa: Artefama - Indústrias Artefama S/A\n",
      "Telefone:+55 (47) 3631-1200\n",
      "Site:www.artefama.com.br\n",
      "E-mail:pacheco@artefama.com.br \n",
      "----------------------------------------\n",
      "Empresa: Artemobili Ltda\n",
      "Telefone:+55 (54) 3242-1890\n",
      "Site:www.artemobili.com.br\n",
      "E-mail:josiane.laurindo@artemobili.com.br \n",
      "----------------------------------------\n",
      "Empresa: Arteobjetos - Uberdecor Moveis e Decorações Eireli\n",
      "Telefone:+55 (34) 3312-6194\n",
      "Site:www.arteobjetos.com.br\n",
      "E-mail:gilberto@arteobjetos.com.br \n",
      "----------------------------------------\n",
      "Empresa: Artesania Actual - Mourão e Cia Ltda.\n",
      "Telefone:+55 (41) 3649-1470\n",
      "Site:www.artesaniaactual.com.br\n",
      "E-mail:artesaniaactual@uol.com.br \n",
      "----------------------------------------\n",
      "Empresa: ARTIMAGE\n",
      "Telefone:+55 (11) 5525-3800 (11) 5521-0834\n",
      "Site:www.artimage.com.br\n",
      "E-mail:cristiane@artimage.com.br \n",
      "----------------------------------------\n",
      "Empresa: Asiatex\n",
      "Telefone:+55 (11) 2423-3333\n",
      "Site:www.asiatex.com.br\n",
      "E-mail:contato@asiatex.com.br \n",
      "----------------------------------------\n",
      "Empresa: Avanti Tapetes - Snl Industria e Comercio Textil Eireli\n",
      "Telefone:(21) 3198-5100\n",
      "Site:www.avantitapetes.com.br\n",
      "E-mail:slettiere@avantitapetes.com.br \n",
      "----------------------------------------\n",
      "Empresa: Bel Metais Moveis Ltda.\n",
      "Telefone:(47) 3644-8294 Ramal 22,23,29\n",
      "Site:www.belmetais.com.br\n",
      "E-mail:diretoria@belmetais.com.br \n",
      "----------------------------------------\n",
      "Empresa: Bell Arte Indústria de Estofados Ltda.\n",
      "Telefone:+55 (47) 3274-1600\n",
      "Site:www.bellarte.com.br\n",
      "E-mail:comercial@bellarte.com.br \n",
      "----------------------------------------\n",
      "Empresa: Bella Produtos Para Iluminação Ltda-ME\n",
      "Telefone:+55 (11) 5660-2600\n",
      "Site:www.bellailuminacao.com.br\n",
      "E-mail:comercial@bellailuminacao.com.br \n",
      "----------------------------------------\n",
      "Empresa: Bernadete Casa\n",
      "Telefone:+55 (16) 3352-9090\n",
      "Site:www.bernadetecasa.com.br\n",
      "E-mail:bernadetecasa@bernadetecasa.com.br \n",
      "----------------------------------------\n",
      "Empresa: Bolis Design\n",
      "Telefone:+55 (49) 3324-2457\n",
      "Site:www.bolis.com.br\n",
      "E-mail:bolis@bolis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Bonté Móveis\n",
      "Telefone:+55 (54) 3293-3467\n",
      "Site:www.bonte.com.br\n",
      "E-mail:comercial@bonte.com.br \n",
      "----------------------------------------\n",
      "Empresa: BTC Decorações e Presentes Ltda\n",
      "Telefone:+55 (11) 3181-2234\n",
      "Site:www.btcdecor.com.br\n",
      "E-mail:pedidos.net@btcdecor.com.br \n",
      "----------------------------------------\n",
      "Empresa: Buchara Com. Imp. Exp. Ltda.\n",
      "Telefone:+55 (19) 3794-7102\n",
      "Site:www.buchara.com.br\n",
      "E-mail:alessandro@buchara.com.br \n",
      "----------------------------------------\n",
      "Empresa: Butzke Importação e Exportação Ltda.\n",
      "Telefone:+55 (47) 3312-4000\n",
      "Site:www.butzke.com.br\n",
      "E-mail:marketing@butzke.com.br \n",
      "----------------------------------------\n",
      "Empresa: ByArtDesign\n",
      "Telefone:+55 (11) 4723 8585\n",
      "Site:www.byartdesign.com.br\n",
      "E-mail:adm@byartdesign.com.br \n",
      "----------------------------------------\n",
      "Empresa: Cabanna Móveis\n",
      "Telefone:+55 (83) 3245-4450\n",
      "Site:www.cabanna.ind.br\n",
      "E-mail:financeiro@cabanna.ind.br \n",
      "----------------------------------------\n",
      "Empresa: Camacã Design em Madeira Ltda.\n",
      "Telefone:+55 (71) 8224-6911\n",
      "Site:www.camacadesign.com\n",
      "E-mail:euvaldo@camacadesign.com \n",
      "----------------------------------------\n",
      "Empresa: Carppem - Movelim Indústria Moveleira Ltda.\n",
      "Telefone:+55 (43) 3274-5500\n",
      "Site:www.carppem.com.br\n",
      "E-mail:carppem@carppem.com.br \n",
      "----------------------------------------\n",
      "Empresa: Cartago Ind. De Tapetes Ltda.\n",
      "Telefone:19-3816-5009\n",
      "Site:www.cartago.com.br\n",
      "E-mail:contato@cartago.com.br \n",
      "----------------------------------------\n",
      "Empresa: Casa Libre Decor\n",
      "Telefone:+55 (11) 4301-2401\n",
      "Site:www.casalibredecor.com.br\n",
      "E-mail:marcelo@casalibredecor.com.br \n",
      "----------------------------------------\n",
      "Empresa: Casa Mundo\n",
      "Telefone:+55 (16) 3610-9797\n",
      "Site:www.casamundodecor.com.br\n",
      "E-mail:marketing@casamundodecor.com.br \n",
      "----------------------------------------\n",
      "Empresa: Casalecchi Móveis Ltda.\n",
      "Telefone:+55 (19) 3651-9060\n",
      "Site:www.casalecchi.com.br\n",
      "E-mail:vendas@casalecchi.com.br \n",
      "----------------------------------------\n",
      "Empresa: Century\n",
      "Telefone:+55 (44) 3264-8550\n",
      "Site:www.meucentury.com\n",
      "E-mail:contato@meucentury.com \n",
      "----------------------------------------\n",
      "Empresa: Cerâmica Mazzotti Ltda. EPP\n",
      "Telefone:+55 (19) 3581-3962\n",
      "Site:www.ceramicamazzotti.com.br\n",
      "E-mail:contato@ceramicamazzotti.com.br \n",
      "----------------------------------------\n",
      "Empresa: CGS Móveis\n",
      "Telefone:+55 (45) 3264-1801\n",
      "Site:www.cgsmoveis.com.br\n",
      "E-mail:comercial@cgsmoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: China Shopping - Vacheron do Brasil Ltda\n",
      "Telefone:11-5666-7999\n",
      "Site:www.chinashopping.com.br\n",
      "E-mail:chinashopping@uol.com.br \n",
      "----------------------------------------\n",
      "Empresa: Combinare - Majoka Moveis e Estofados Ltda.\n",
      "Telefone:+55 (43) 3303-3100\n",
      "Site:www.combinare.com.br\n",
      "E-mail:carlos@combinare.com.br \n",
      "----------------------------------------\n",
      "Empresa: Companhia das Folhas\n",
      "Telefone:+55 (11) 3831-0300\n",
      "Site:www.ciadasfolhas.com.br\n",
      "E-mail:angela@ciadasfolhas.com.br \n",
      "----------------------------------------\n",
      "Empresa: Cristais di Murano\n",
      "Telefone:+55 (47) 3327-0459\n",
      "Site:www.cristaisdimurano.com.br\n",
      "E-mail:comercial@cristaisdimurano.com.br \n",
      "----------------------------------------\n",
      "Empresa: Cristais São Marcos\n",
      "Telefone:+55 (35) 3697-1892\n",
      "Site:www.cristaissaomarcos.com.br\n",
      "E-mail:vendas@cristaissaomarcos.com.br \n",
      "----------------------------------------\n",
      "Empresa: D Angelis\n",
      "Telefone:+55 (45) 3286-8100 (45) 9972-0582\n",
      "Site:www.anjos.ind.br\n",
      "E-mail:dangelis@anjos.ind.br \n",
      "----------------------------------------\n",
      "Empresa: Daeve Flores e Plantas Pemanentes\n",
      "Telefone:+55 (11) 3208-3515\n",
      "Site:www.daeve.com.br\n",
      "E-mail:contato@daeve.com.br \n",
      "----------------------------------------\n",
      "Empresa: Deco Inside and Outside\n",
      "Telefone:+55 (43) 3253-1267\n",
      "Site:www.decometal.com.br\n",
      "E-mail:decometal@decometal.com.br \n",
      "----------------------------------------\n",
      "Empresa: Decorare Textil Ltda.\n",
      "Telefone:83-3245-3344\n",
      "Site:www.decorareonline.com.br\n",
      "E-mail:vendas2@decorareonline.com.br \n",
      "----------------------------------------\n",
      "Empresa: Decorative\n",
      "Telefone:+55 (11) 3361-2401\n",
      "Site:\n",
      "E-mail:sanslemes@gmail.com \n",
      "----------------------------------------\n",
      "Empresa: Decortextil\n",
      "Telefone:+55 (19) 3478-5005\n",
      "Site:www.decortextil.com.br\n",
      "E-mail:vendas@decortextil.com.br \n",
      "----------------------------------------\n",
      "Empresa: Delinear\n",
      "Telefone:+55 (11) 2015-4651\n",
      "Site:www.delinearmoveis.com.br\n",
      "E-mail:renan@delinearmoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Desigan Indústria e Comércio de Móveis Ltda\n",
      "Telefone:41-3677-2525\n",
      "Site:www.desigan.com.br\n",
      "E-mail:desigan@desigan.com.br \n",
      "----------------------------------------\n",
      "Empresa: Destack Móveis\n",
      "Telefone:+55 (17) 3422-4040\n",
      "Site:www.dkline.com.br\n",
      "E-mail:ederval@destackmoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: DF Decor\n",
      "Telefone:+55 (54) 98435-5408\n",
      "Site:\n",
      "E-mail:dfdecormoveis@gmail.com \n",
      "----------------------------------------\n",
      "Empresa: DiBrianza\n",
      "Telefone:+55 (41) 3272-0380\n",
      "Site:www.dibrianza.com.br\n",
      "E-mail:contato@dibrianza.com.br \n",
      "----------------------------------------\n",
      "Empresa: Doimo Brasil\n",
      "Telefone:+55 (31) 3626-9350\n",
      "Site:www.doimobrasil.com.br\n",
      "E-mail:recepcao@doimobrasil.com.br \n",
      "----------------------------------------\n",
      "Empresa: Eduardo Moraes\n",
      "Telefone:+55 (21) 2716-5533\n",
      "Site:www.eduardomoraesimport.com.br\n",
      "E-mail:administrativo1@teratai.com.br \n",
      "----------------------------------------\n",
      "Empresa: Elisê Móveis Ltda.\n",
      "Telefone:+55 (54) 3281-9012\n",
      "Site:www.elise.com.br\n",
      "E-mail:comercial@elise.com.br \n",
      "----------------------------------------\n",
      "Empresa: Empório Tapetes\n",
      "Telefone:+55 (48) 3015-5010\n",
      "Site:www.emporiotapetes.com.br\n",
      "E-mail:comercial_dws@emporiotapetes.com.br \n",
      "----------------------------------------\n",
      "Empresa: Emporio Tiffany - Due Vetri Moveis e Artigos de Decoração Ltda-ME\n",
      "Telefone:+55 (11) 3445-2329\n",
      "Site:www.lucamilani.com.br\n",
      "E-mail:duevetridecor@gmail.com \n",
      "----------------------------------------\n",
      "Empresa: Emporio Tiffany - Serbin Indústria e Comercial Ltda\n",
      "Telefone:+55 (11) 3588-4002\n",
      "Site:www.emporiotiffany.com.br\n",
      "E-mail:miguel@emporiotiffany.com.br \n",
      "----------------------------------------\n",
      "Empresa: Entrecasa\n",
      "Telefone:+55 (71) 3016-6334\n",
      "Site:www.entrecasa.com.br\n",
      "E-mail:representanteentrecasa@hotmail.com \n",
      "----------------------------------------\n",
      "Empresa: Escal\n",
      "Telefone:+55 (49) 3322-2132\n",
      "Site:www.escalmoveis.com.br\n",
      "E-mail:altemir@escalmoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Essenza Design\n",
      "Telefone:(54) 3293.1077\n",
      "Site:www.essenzadesign.com.br\n",
      "E-mail:comercial@essenzadesign.com.br \n",
      "----------------------------------------\n",
      "Empresa: Estobel Indústria de Estofados Ltda.\n",
      "Telefone:+55 (54) 2109-3000\n",
      "Site:www.estobel.com\n",
      "E-mail:estobel@estobel.com.br \n",
      "----------------------------------------\n",
      "Empresa: Estofados Enele\n",
      "Telefone:+55 (49) 3344-8999\n",
      "Site:www.enele.com.br\n",
      "E-mail:anamaria@enele.com.br \n",
      "----------------------------------------\n",
      "Empresa: Estofados Imperial-Casavetti\n",
      "Telefone:+55 (54) 3454-9799\n",
      "Site:www.vilaimperial.com.br\n",
      "E-mail:vila.adm@vilaimperial.com.br \n",
      "----------------------------------------\n",
      "Empresa: Estofados Jardim Ltda.\n",
      "Telefone:+55 (47) 2106-7599\n",
      "Site:www.estofadosjardim.com.br\n",
      "E-mail:jardim@estofadosjardim.com.br \n",
      "----------------------------------------\n",
      "Empresa: Estofados Mannes\n",
      "Telefone:+55 (47) 3373-9200\n",
      "Site:www.mannes.com.br\n",
      "E-mail:marcio@estofadosmannes.com.br \n",
      "----------------------------------------\n",
      "Empresa: Estofados Tironi Ltda.\n",
      "Telefone:+55 (47) 3370-4077\n",
      "Site:www.estofadostironi.com.br\n",
      "E-mail:richard@estofadostironi.com.br \n",
      "----------------------------------------\n",
      "Empresa: Estofados Treviso Ltda.\n",
      "Telefone:+55 (54) 3477-1215\n",
      "Site:www.estofadostreviso.com.br\n",
      "E-mail:estofadostreviso@estofadostreviso.com.br \n",
      "----------------------------------------\n",
      "Empresa: Feeling Estofados Ltda.\n",
      "Telefone:+55 (47) 3376-1300\n",
      "Site:www.feelingestofados.com.br\n",
      "E-mail:feeling@feelingestofados.com.br \n",
      "----------------------------------------\n",
      "Empresa: Fibras Arte - Artes Primavera Móv.Ind.Com.Ltda\n",
      "Telefone:+55 (21) 2676-3787\n",
      "Site:www.fibrasarte.com.br\n",
      "E-mail:cristiane.alves@fibrasarte.com.br \n",
      "----------------------------------------\n",
      "Empresa: Flor de Liz Imports Ltda - EPP\n",
      "Telefone:(54) 3225-6830\n",
      "Site:www.flordelizimports.com.br\n",
      "E-mail:comercial@flordelizimports.com.br \n",
      "----------------------------------------\n",
      "Empresa: Formanova Ind. E Com. De Móveis Ltda.\n",
      "Telefone:+55 (48) 3242-3099 (48) 3286-0644\n",
      "Site:www.formanovamoveis.com.br\n",
      "E-mail:formanova@formanovamoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Formline Móveis\n",
      "Telefone:+55 (44) 3268-1878\n",
      "Site:www.formlinemoveis.com.br\n",
      "E-mail:formline@terra.com.br \n",
      "----------------------------------------\n",
      "Empresa: Frontier Importadora\n",
      "Telefone:+55 (17) 3213-9600\n",
      "Site:www.frontierimportadora.com.br\n",
      "E-mail:admin@frontierimportadora.com.br \n",
      "----------------------------------------\n",
      "Empresa: Fuzimoto - Fabio Fuzimoto ME.\n",
      "Telefone:+55 (11) 45941361\n",
      "Site:www.fabiofuzi.com.br\n",
      "E-mail:vendas@fabiofuzi.com.br \n",
      "----------------------------------------\n",
      "Empresa: German Interiores\n",
      "Telefone:+55 (61) 3354-7979\n",
      "Site:www.german.com.br\n",
      "E-mail:german@german.com.br \n",
      "----------------------------------------\n",
      "Empresa: Germânia Moveis e Decoração\n",
      "Telefone:+55 (54) 3281-8250\n",
      "Site:www.germania.com.br\n",
      "E-mail:germania@germania.com.br \n",
      "----------------------------------------\n",
      "Empresa: Gold Line Ind. e Com. de Móveis e Estofados Ltda\n",
      "Telefone:+55 (44) 3032-9100\n",
      "Site:www.goldline.ind.br\n",
      "E-mail:goldline@goldline.ind.br \n",
      "----------------------------------------\n",
      "Empresa: Goods BR Distribuidora Ltda - ME\n",
      "Telefone:54 32955300\n",
      "Site:www.goodsbr.com.br\n",
      "E-mail:josue@goodsbr.com.br \n",
      "----------------------------------------\n",
      "Empresa: GS Móveis\n",
      "Telefone:(41) 3372-1216\n",
      "Site:www.gsmoveis.com.br\n",
      "E-mail:gsmoveis@gsmoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Ha. Fatto\n",
      "Telefone:+55 (47) 3318-0800\n",
      "Site:www.hafatto.com.br\n",
      "E-mail:marketing@seatshome.com.br \n",
      "----------------------------------------\n",
      "Empresa: Hariz Comércio de Tapetes Ltda.\n",
      "Telefone:+55 (11) 5053-7700\n",
      "Site:www.hariz.com.br\n",
      "E-mail:melhem@hariz.com.br \n",
      "----------------------------------------\n",
      "Empresa: Helizart Ltda\n",
      "Telefone:+55 (31) 3227-9613\n",
      "Site:www.helizart.com.br\n",
      "E-mail:helizart@helizart.com.br \n",
      "----------------------------------------\n",
      "Empresa: Herval Móveis e Colchões\n",
      "Telefone:+55 (51) 3564-8300\n",
      "Site:www.moveisherval.com.br\n",
      "E-mail:alberto.machado@herval.com.br \n",
      "----------------------------------------\n",
      "Empresa: Home Collection\n",
      "Telefone:+55 (11) 3826-0077\n",
      "Site:www.homecollection.com.br\n",
      "E-mail:vendas@homecollection.com.br \n",
      "----------------------------------------\n",
      "Empresa: Im In\n",
      "Telefone:+55 (12) 2125 1869\n",
      "Site:www.iminhome.com.br\n",
      "E-mail:maria@iminhome.com.br \n",
      "----------------------------------------\n",
      "Empresa: Itamoveis Industria e Comercio Ltda - ME\n",
      "Telefone:+55 (47) 3644-3597\n",
      "Site:-\n",
      "E-mail:comercial@itamoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: IUMMI.\n",
      "Telefone:+55 (54) 2621-7030\n",
      "Site:www.iummi.com.br\n",
      "E-mail:vendas@iummi.com.br \n",
      "----------------------------------------\n",
      "Empresa: Jowanel Móveis\n",
      "Telefone:+55 (17)3411-1400\n",
      "Site:www.jowanel.com.br\n",
      "E-mail:jowanel@jowanel.com.br \n",
      "----------------------------------------\n",
      "Empresa: K & F Comércio de Tapetes e Artigos de Decoração\n",
      "Telefone:+55 (11) 3825-0199\n",
      "Site:\n",
      "E-mail:henrique@kftapetes.com.br \n",
      "----------------------------------------\n",
      "Empresa: KZ Home Stock\n",
      "Telefone:(11) 2284-8888\n",
      "Site:www.kzhomestock.com.br\n",
      "E-mail:anna@kzhomestock.com.br \n",
      "----------------------------------------\n",
      "Empresa: Laform Estofados Ltda.\n",
      "Telefone:+55 (54) 3285-1690\n",
      "Site:www.laform.com.br\n",
      "E-mail:estevao@laform.com.br \n",
      "----------------------------------------\n",
      "Empresa: Lazzari Móveis\n",
      "Telefone:(54) 3464-8800\n",
      "Site:www.lazzinterni.com.br\n",
      "E-mail:comercial@lazzarimoveis.com \n",
      "----------------------------------------\n",
      "Empresa: Les Coussins\n",
      "Telefone:+55 (19) 3295-7437\n",
      "Site:www.lescoussins.com.br\n",
      "E-mail:contato@lescoussins.com.br \n",
      "----------------------------------------\n",
      "Empresa: Liberal Marini - AM Liberal Decorações Ltda\n",
      "Telefone:+55 (21)993347452\n",
      "Site:www.liberalmarini.com\n",
      "E-mail:contato@liberalmarini.com \n",
      "----------------------------------------\n",
      "Empresa: Linea Home\n",
      "Telefone:(11) 98449-0072\n",
      "Site:www.lineahome.com.br\n",
      "E-mail:vendas@lineahome.com.br \n",
      "----------------------------------------\n",
      "Empresa: Lovato Moveis Eireli Epp\n",
      "Telefone:+55 (41) 3677-2805\n",
      "Site:www.lovatomoveis.com.br\n",
      "E-mail:denise@lovatomoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Lucatti Artes e Decorações Ltda\n",
      "Telefone:+55 (13) 3313-1747\n",
      "Site:www.lucattiartes.com\n",
      "E-mail:atendimento@lucattiartes.com \n",
      "----------------------------------------\n",
      "Empresa: Madeplan Design\n",
      "Telefone:+55 (48) 3658-8584\n",
      "Site:www.madeplan.ind.br\n",
      "E-mail:edina@madeplan.ind.br \n",
      "----------------------------------------\n",
      "Empresa: Maiori Casa\n",
      "Telefone:+55 (11) 2423-3333\n",
      "Site:www.maioricasa.com.br\n",
      "E-mail:contato@maioricasa.com.br \n",
      "----------------------------------------\n",
      "Empresa: Maisofa Estofados\n",
      "Telefone:+55  (47) 3634-2723\n",
      "Site:www.maisofa.com.br\n",
      "E-mail:contato@maisofa.com.br \n",
      "----------------------------------------\n",
      "Empresa: MATREZAN DECOR\n",
      "Telefone:+55 (54) 3275-1225\n",
      "Site:www.matrezan.com.br\n",
      "E-mail:fiorin@matrezan.com.br \n",
      "----------------------------------------\n",
      "Empresa: Melyana Comércio Ltda.\n",
      "Telefone:+55 (21) 2527-8020\n",
      "Site:www.melyana.com.br\n",
      "E-mail:melyana@melyana.com.br \n",
      "----------------------------------------\n",
      "Empresa: Mempra Design\n",
      "Telefone:+55 (43) 3174-6600\n",
      "Site:www.mempra.com.br\n",
      "E-mail:bruno@mempra.com.br \n",
      "----------------------------------------\n",
      "Empresa: Mestre Artesão\n",
      "Telefone:+55 (43) 3328-8143\n",
      "Site:www.mestreartesao.com.br\n",
      "E-mail:contato@mestreartesao.com.br \n",
      "----------------------------------------\n",
      "Empresa: Mobilier Indústria e Comércio de Móveis Ltda.\n",
      "Telefone:+55 (48) 3286-3698\n",
      "Site:\n",
      "E-mail:alex@mobilierdecor.com.br \n",
      "----------------------------------------\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empresa: Modali Design\n",
      "Telefone:+55 (11) 3661-2200\n",
      "Site:www.modali.com.br\n",
      "E-mail:denise@modali.com.br \n",
      "----------------------------------------\n",
      "Empresa: Modalle Móveis\n",
      "Telefone:+55 (17) 3421-9186\n",
      "Site:www.modalle.com.br\n",
      "E-mail:mariluci@modalle.com.br \n",
      "----------------------------------------\n",
      "Empresa: Móveis Cacique\n",
      "Telefone:+55 (35) 3531-1559\n",
      "Site:www.moveiscacique.com.br\n",
      "E-mail:contato@moveiscacique.com.br \n",
      "----------------------------------------\n",
      "Empresa: Móveis Cosmo\n",
      "Telefone:+55 (17) 3426-7600\n",
      "Site:www.cosmo.ind.br\n",
      "E-mail:thais@cosmo.ind.br \n",
      "----------------------------------------\n",
      "Empresa: Móveis Irimar Industria e Comércio Ltda\n",
      "Telefone:+55 (47) 3644-2599\n",
      "Site:www.irimar.com.br\n",
      "E-mail:vianei.zappellini@irimar.com.br \n",
      "----------------------------------------\n",
      "Empresa: Móveis James Ltda.\n",
      "Telefone:+55 (47) 3631-0300\n",
      "Site:www.moveisjames.com.br\n",
      "E-mail:comercial@moveisjames.com.br \n",
      "----------------------------------------\n",
      "Empresa: Móveis Rafana\n",
      "Telefone:+55 (32) 3531-1458\n",
      "Site:www.rafanamoveis.com.br\n",
      "E-mail:mc.supervisao@gmail.com \n",
      "----------------------------------------\n",
      "Empresa: Móveis Rudnick S/A\n",
      "Telefone:+55 (47) 3631-1000\n",
      "Site:www.rudnick.com.br\n",
      "E-mail:marketing@rudnick.com.br \n",
      "----------------------------------------\n",
      "Empresa: Movelaria Coisas do Brasil\n",
      "Telefone:+55 (34) 3318-2100\n",
      "Site:www.reginez.com.br\n",
      "E-mail:vendas@reginez.com.br \n",
      "----------------------------------------\n",
      "Empresa: Msul Ind. de Moveis Ltda.\n",
      "Telefone:+55 (54) 3477-2274\n",
      "Site:www.msulmoveis.com.br\n",
      "E-mail:arthur@msulmoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Neoali Brasil Art\n",
      "Telefone:+55 (45) 3240-2119\n",
      "Site:www.neoali.com.br\n",
      "E-mail:neoali@neoali.com.br \n",
      "----------------------------------------\n",
      "Empresa: Nova Home Comércio e Distribuição Ltda - EPP\n",
      "Telefone:+55 (21) 3158-9534\n",
      "Site:www.novahome.com.br\n",
      "E-mail:contato@novahome.com.br \n",
      "----------------------------------------\n",
      "Empresa: O Galpão\n",
      "Telefone:+55 (21) 2254-5400\n",
      "Site:www.ogalpao.com.br\n",
      "E-mail:suzana@galpaomoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Officina Móveis\n",
      "Telefone:+55 (54) 3282-1290\n",
      "Site:www.officinamoveisgramado.com.br\n",
      "E-mail:vendas@officinamoveisgramado.com.br \n",
      "----------------------------------------\n",
      "Empresa: Oficina J. Mangabeira\n",
      "Telefone:+55 (19) 3867-1275\n",
      "Site:www.jmangabeira.com.br\n",
      "E-mail:carlos@jmangabeira.com.br \n",
      "----------------------------------------\n",
      "Empresa: Old Compton\n",
      "Telefone:+55 (32) 3331.6914\n",
      "Site:www.hobnob.com.br\n",
      "E-mail:hobnob@hobnob.com.br \n",
      "----------------------------------------\n",
      "Empresa: ÓR Design\n",
      "Telefone:+55 (11) 2606-0511\n",
      "Site:www.ordesign.com.br\n",
      "E-mail:ricardo@ordesign.com.br \n",
      "----------------------------------------\n",
      "Empresa: Orbhes Espumas e Colchoes Ltda.\n",
      "Telefone:+55 (47) 3376-8400\n",
      "Site:www.orbhes.com.br\n",
      "E-mail:laercio@feelingestofados.com.br \n",
      "----------------------------------------\n",
      "Empresa: Parma Móveis Ltda.\n",
      "Telefone:+55 (32) 3539-2500\n",
      "Site:www.parmamoveis.com.br\n",
      "E-mail:marianna@parmamoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Pollo Industria e Transporte de Moveis Ltda\n",
      "Telefone:+55 (32) 3532-8842\n",
      "Site:www.pollodecor.com.br\n",
      "E-mail:comercial@pollodecor.com.br \n",
      "----------------------------------------\n",
      "Empresa: Pollus Móveis\n",
      "Telefone:+55 (17) 3426-1234\n",
      "Site:www.pollusmoveis.com.br\n",
      "E-mail:pollus@pollusmoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Quadrum & Arte\n",
      "Telefone:+55 (11) 3222.7612\n",
      "Site:www.quadrumeart.com.br\n",
      "E-mail:quadroecor@uol.com.br \n",
      "----------------------------------------\n",
      "Empresa: Recliners Industrial Ltda.\n",
      "Telefone:+55 (19) 3486-7512\n",
      "Site:www.recliners.com.br\n",
      "E-mail:recliners@recliners.com.br \n",
      "----------------------------------------\n",
      "Empresa: Renar Móveis S/A\n",
      "Telefone:+55 (49) 3246-591\n",
      "Site:www.renar.com.br\n",
      "E-mail:marcelo@renar.com.br \n",
      "----------------------------------------\n",
      "Empresa: Ribeiro & Pavani\n",
      "Telefone:11-3414-1000\n",
      "Site:www.ribeiroepavani.com.br\n",
      "E-mail:central@ribeiroepavani.com.br \n",
      "----------------------------------------\n",
      "Empresa: Rivatti Móveis Ltda.\n",
      "Telefone:+55 (54) 3025-9300\n",
      "Site:www.rivatti.com.br\n",
      "E-mail:vendas@rivatti.com.br \n",
      "----------------------------------------\n",
      "Empresa: Rosa Maria Decorações Eireli.\n",
      "Telefone:+55 (54) 3462-4932\n",
      "Site:www.rosamariadecoracao.com.br\n",
      "E-mail:rosamariadecoracao@gmail.com \n",
      "----------------------------------------\n",
      "Empresa: Safari\n",
      "Telefone:+55 (41) 3543-1212\n",
      "Site:safari@safarimoveis.com.br\n",
      "E-mail:safari@safarimoveis.com.br \n",
      "----------------------------------------\n",
      "Empresa: Salva Design de Mobiliário - Salvatore Minuano\n",
      "Telefone:+55 (51) 3552-2500\n",
      "Site:www.salvamobiliario.com.br\n",
      "E-mail:thiago@estofadosminuano.com.br \n",
      "----------------------------------------\n"
     ]
    },
    {
     "ename": "UnicodeEncodeError",
     "evalue": "'charmap' codec can't encode character '\\u0301' in position 27: character maps to <undefined>",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnicodeEncodeError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-28-0ac6599b0825>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf'E-mail:{email}'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'-'\u001b[0m\u001b[1;33m*\u001b[0m\u001b[1;36m40\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m     \u001b[0mcsv_writer\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwriterow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mid\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mempresa\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtelefone\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0msite\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0memail\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m     \u001b[0mid\u001b[0m\u001b[1;33m+=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\encodings\\cp1252.py\u001b[0m in \u001b[0;36mencode\u001b[1;34m(self, input, final)\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mIncrementalEncoder\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcodecs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mIncrementalEncoder\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     18\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mencode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfinal\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 19\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mcodecs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcharmap_encode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mencoding_table\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     20\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     21\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mIncrementalDecoder\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcodecs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mIncrementalDecoder\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mUnicodeEncodeError\u001b[0m: 'charmap' codec can't encode character '\\u0301' in position 27: character maps to <undefined>"
     ]
    }
   ],
   "source": [
    "id = 0\n",
    "for elemento in todos_elementos:\n",
    "    empresa = elemento.h5.text\n",
    "    telefone = elemento.find('i',class_= 'fa-phone').next_element.next_element.text\n",
    "    site = elemento.find('i',class_= 'fa-link').next_element.next_element.text\n",
    "    email = elemento.find('i',class_= 'fa-at').next_element.next_element.text\n",
    "    print(f'Empresa: {empresa}')\n",
    "    print(f'Telefone:{telefone}')\n",
    "    print(f'Site:{site}')\n",
    "    print(f'E-mail:{email}')\n",
    "    print('-'*40)\n",
    "    csv_writer.writerow([id,empresa,telefone,site,email])\n",
    "    id+=1\n",
    "    \n",
    "csv_file.close()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
