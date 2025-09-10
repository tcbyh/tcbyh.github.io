# arxiv_liter

arxiv 文献整理工具

- **fetch**: download arxiv paper pdf with url
- **sync**: collect and organize paper urls in markdown, automatically download pdfs and update markdown content

## Install

requirements: Python >= 3.9

```
git clone https://github.com/tcbyh/candp.git
cd candp
pip install [-v -e] toolbox/arxiv_liter
```

## Example

```
arxiv_liter fetch https://arxiv.org/abs/1706.03762

arxiv_liter sync ./tests/mds/test.md
```

## Rule

test.md
```
- {{https://arxiv.org/abs/1706.03762}}
- ResNet: {{https://arxiv.org/abs/1512.03385}}
```

pdf save name: first paper will use full title, second paper will use alias title -- "ResNet"


# Acknowledgements

- https://github.com/wilmerwang/autoLiterature
