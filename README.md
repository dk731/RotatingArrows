# Fourie transform visualisation

### Main idea and inspiration behid this project is from this video : https://bit.ly/2FG92AM

## Basic information

This is python script that represents simplified version of function (supports svg path) , by representing it with many arrows that are attached to eachs's other ends. All of this lines have their unique start position and constant roation speed.

## Usage

- Prepear svg file as show in Horse.svg, it should include one path in a shape that you want to use
- Run python script ("rotating_arrows.py") passing path to svg as a argument.

      python rotating_arrows.py ./Horse.svg

- Have Fun!

## Additional infomation

_You can change paramets in source file to get other intresing results. For example_

- In line 32, change variable _prec_of_inter_ to increase or decrease of drawn points

```python
prec_of_inter = 10000
```

- In line 41, change variable _prec_ to control amount of arrows

```python
prec = 10
```

### Some example screenshots

- _3 arrows:_

![alt text][img1]

- _20 arrows:_

![alt text][img2]

- _100 arrows_

![alt text][img3]

[img1]: images/3_arrows_example.png
[img2]: images/20_arrows_example.png
[img3]: images/100_arrows_example.png
