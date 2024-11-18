# Dọc Kinh Thánh

[![pages-build-deployment](https://github.com/kreier/kinhthanh/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/kreier/kinhthanh/actions/workflows/pages/pages-build-deployment)

Những điểm nổi bật trong bài đọc Kinh Thánh

Dự án này được lấy cảm hứng từ [dự án tiếng Anh này](https://github.com/kreier/study). Và tất nhiên là [bản dịch tiếng Việt](https://timeline24.github.io/timeline_vi.pdf) của [dự án dòng thời gian](https://github.com/kreier/timeline).

![timeline project](https://raw.githubusercontent.com/kreier/timeline/main/docs/timeline20240516_4.6.png)

## Lịch sử

- 2023/12/22 Bắt đầu dự án này bằng tiếng Việt. Kho lưu trữ này đã được tạo.
- 2024/10/30 Tài liệu tập tin âm thanh cho [tiếng Anh](https://github.com/kreier/kinhthanh/blob/main/data/size_audio_en.csv) và [tiếng Việt](https://github.com/kreier/kinhthanh/blob/main/data/size_audio_vi.csv).
- 2024/11/18 Tài liệu về các tập tin [âm thanh bằng tiếng Đức](https://github.com/kreier/kinhthanh/blob/main/data/size_audio_de.csv). 

## Support for $\LaTeX$ and math formula

$$
f(x) = \int_0^{2\pi}\sin\phi e^{i\pi\theta}
$$

inline: $$f(x) = \int_{-\infty}^\infty \hat f(\xi)\,e^{2 \pi i \xi x} \,d\xi$$

display mode (centered):

$$f(x) = \int_{-\infty}^\infty \hat f(\xi)\,e^{2 \pi i \xi x} \,d\xi$$

## Mermaid

``` mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
```

## Plotly

``` plotly
{
  "data": [
    {
      "line": {"shape": "linear"},
      "mode": "lines+markers",
      "name": "linear",
      "type": "scatter",
      "x": [1, 2, 3, 4, 5],
      "y": [1, 3, 2, 3, 1],
      "hoverinfo": "name"
    },
    {
      "line": {"shape": "spline"},
      "mode": "lines+markers",
      "name": "spline",
      "type": "scatter",
      "x": [1, 2, 3, 4, 5],
      "y": [6, 8, 7, 8, 6],
      "text": ["tweak line smoothness<br>with 'smoothing' in line object"],
      "hoverinfo": "text+name"
    },
    {
      "line": {"shape": "vhv"},
      "mode": "lines+markers",
      "name": "vhv",
      "type": "scatter",
      "x": [1, 2, 3, 4, 5],
      "y": [11, 13, 12, 13, 11],
      "hoverinfo": "name"
    },
    {
      "line": {"shape": "hvh"},
      "mode": "lines+markers",
      "name": "hvh",
      "type": "scatter",
      "x": [1, 2, 3, 4, 5],
      "y": [16, 18, 17, 18, 16],
      "hoverinfo": "name"
    },
    {
      "line": {"shape": "vh"},
      "mode": "lines+markers",
      "name": "vh",
      "type": "scatter",
      "x": [1, 2, 3, 4, 5],
      "y": [21, 23, 22, 23, 21],
      "hoverinfo": "name"
    },
    {
      "line": {"shape": "hv"},
      "mode": "lines+markers",
      "name": "hv",
      "type": "scatter",
      "x": [1, 2, 3, 4, 5],
      "y": [26, 28, 27, 28, 26],
      "hoverinfo": "name"
    }
  ],
  "layout": {
    "legend": {
      "y": 0.5,
      "font": {"size": 16},
      "traceorder": "reversed"
    }
  }
}
```


## Chartjs

``` chartjs
{
  "config": {
    "type": "line",
    "data": {
      "labels": [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
      "datasets": [{
          "data": [86,114,106,106,107,111,133,221,783,2478],
          "label": "Africa",
          "borderColor": "#3e95cd",
          "fill": false
        }, {
          "data": [282,350,411,502,635,809,947,1402,3700,5267],
          "label": "Asia",
          "borderColor": "#8e5ea2",
          "fill": false
        }, {
          "data": [168,170,178,190,203,276,408,547,675,734],
          "label": "Europe",
          "borderColor": "#3cba9f",
          "fill": false
        }, {
          "data": [40,20,10,16,24,38,74,167,508,784],
          "label": "Latin America",
          "borderColor": "#e8c3b9",
          "fill": false
        }, {
          "data": [6,3,2,2,7,26,82,172,312,433],
          "label": "North America",
          "borderColor": "#c45850",
          "fill": false
        }
      ]
    },
    "options": {
      "title": {
        "display": true,
        "text": "World population per region (in millions)"
      }
    }
  }
}
```

