# HomeCredit - Credit Risk Model Stability

Current status: initated

## Motivation

Found the **HomeCredit - Credit Risk Model Stability** competition through a [post](https://www.linkedin.com/feed/update/urn:li:activity:7202186950538129408/) on Linked In by and [Tri Duc Nguyen Tang](https://www.linkedin.com/in/tri-duc-n-099528133/), although it's was late for submission but let's see how can I build a model from this data.

**Link to competition**: <https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability/overview>

## Setup

```bash
uv venv
.venv/Scripts/activate
uv sync
```

## Make the data ready

1. Install `kaggle` by specify it in the `pyproject.toml`;
2. Activate your environment (for eg. `.venv/Script/activate`);
3. Navigate to this folder (`./src/data`) and run: `kaggle competitions download -c home-credit-credit-risk-model-stability`;
4. Run the `data_setup.py` on the parent folder.

## References

1. Baseline notebook: <https://www.kaggle.com/code/greysky/home-credit-baseline/notebook>;
2. Early EDA and submission: <https://www.kaggle.com/code/sergiosaharovskiy/home-credit-crms-2024-eda-and-submission>;
3. 10th place discussion: <https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability/discussion/508588>;
4. 1st place discussion: <https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability/discussion/508337>.
