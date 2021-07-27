# devnagri-pdf-text

## ए॒वमुप॑युज्यते

```shell
ttx NotoSansDevanagari-Regular.ttf
```

ततः `python-shell`-म॒ध्ये

```python
import devnagri_pdf_text
f = devnagri_pdf_text.Font('NotoSansDevanagari-Regular.ttx')
print(f.id_unicode([57, 39, 463], prkriya = True))
```

इ॒दं ल॑भ्यते

```
vadeva
nnadeva
धात॑वः ovowelsignrephanusvaradeva > ovowelsigndeva + rephanusvaradeva
ovowelsigndeva
धात॑वः rephanusvaradeva > rephdeva + anusvaradeva
धात॑वः rephdeva > radeva + viramadeva
radeva
viramadeva
anusvaradeva
वणोर्ं
```