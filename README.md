# assignments

coursework graveyard — AdvML, ImageProcessing, InformationRetrieval, Numerical Methods, plus a CV cameo.

```
.
├── AdvML/                          # advanced ml shenanigans
│   ├── cls.ipynb                   # classification pog
│   ├── datarep.ipynb               # data representation who
│   ├── delhicli.ipynb              # delhi climate — LSTM go brrr
│   ├── gaussianbayes.ipynb         # gaussian nb
│   ├── lstmcli.pt                  # trained LSTM checkpoint flex
│   ├── spambayes.ipynb             # "is this spam?" — bayes says yes
│   ├── spatialfilters.ipynb        # kernels go brrr
│   ├── stdlstmtutorial.ipynb       # LSTM tutorial
│   ├── stdperformance.ipynb        # student performance regression
│   ├── timeserieslab.ipynb         # time series torture
│   ├── spam.csv, studentperformance.csv, DailyDelhiClimate*.csv
│
├── ImageProcessing/                # pixels, kernels, opencv shenanigans
│   ├── lab1_basic...               # reading/writing pixels
│   ├── lab2_point_processing       # histograms, contrast stretching
│   ├── lab3_spatial_filtering      # blur/sharpen/edge detect
│   ├── lab4_morphological          # erode/dilate/open/close
│   └── color_image_processing      # HSV, YCrCb, color channels
│
├── InformationRetrieval/           # "did you mean?" the lab
│   ├── Lab1_Precision_Recall_F1    # metrics 101
│   ├── Lab2_MAP_nDCG               # ranking metrics
│   └── Lab3_BIM_BM25               # probabilistic IR
│
├── Numerical\ Methods/             # float go brrr, convergence who?
│   ├── trapezoidal.py              # basic numerical integration
│   ├── simpson1.py                 # simpson's 1/3 rule
│   ├── simpson2.py                 # simpson's 3/8 rule
│   ├── doubletrapezoidal.py        # 2D trapezoidal
│   └── dlbsimpson.py               # double simpson
│
├── cvtest.ipynb                    # license plate detection — YOLO + EasyOCR ANPR
├── input.mp4                       # raw dashcam footage
├── output.mp4                      # detected plates with OCR text overlay
│
└── README.md                       # you are here
```

the usual: jupyter notebooks, `.py` scripts, latex reports, and a prayer that the grader runs the right kernel torch version.

> **vibe check**: AdvML is LSTM city × 3, ImageProcessing is lab-by-lab opencv 101, IR is all ranking all the time, NumMethods is simpson's infinite variants, and cvtest.py snuck in a full ANPR pipeline.

> "works on my machine"™ — `torch.compile` not included
