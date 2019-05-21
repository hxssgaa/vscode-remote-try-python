#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import torch
import numpy as np
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    x = np.array(list(range(200)))
    x = torch.tensor(x, dtype=torch.float64, device=device)
    y = x ** 2
    return app.send_static_file("index.html")
