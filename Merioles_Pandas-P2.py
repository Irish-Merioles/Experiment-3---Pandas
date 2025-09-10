{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f30eca2d-f97f-48ac-af4c-044fad3f9c5f",
   "metadata": {},
   "source": [
    "### Pandas-P2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6189d1b7-1c69-4583-9717-e36cfc1f6099",
   "metadata": {},
   "source": [
    "###  Merioles, Irish Rianne T."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e056527f-44f3-4b37-acd0-f631afcdf0c8",
   "metadata": {},
   "source": [
    "### 2ECEB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9c52b04-f602-417b-a169-ccd31deeec7b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e5fe3496-e560-4e55-9798-c980bdc580e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60daf024-6c55-476b-aac1-df649c36417d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0d15c9af-048a-47e7-a5c8-6ca6048a8556",
   "metadata": {},
   "outputs": [],
   "source": [
    "cars = pd.read_csv('Cars.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "af64be1d-2540-4c28-819c-0ce0f7eed2a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Model  cyl   hp     wt  vs  gear\n",
      "0          Mazda RX4    6  110  2.620   0     4\n",
      "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
      "2         Datsun 710    4   93  2.320   1     4\n",
      "3     Hornet 4 Drive    6  110  3.215   1     3\n",
      "4  Hornet Sportabout    8  175  3.440   0     3\n"
     ]
    }
   ],
   "source": [
    "print(cars.iloc[:5, ::2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "43909b92-6cc4-4991-991c-44b0bd6737ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
      "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4\n"
     ]
    }
   ],
   "source": [
    "print(cars[cars['Model'] == 'Mazda RX4'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8b24b186-648c-451e-8a91-22e86c84b583",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "print(cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4e0dc80b-3c02-4388-9208-8021678a588e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']\n",
    "print(cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a05398c3-c6ce-4ef2-b28d-d3554a83389e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
