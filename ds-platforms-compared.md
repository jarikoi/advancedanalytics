|   | ![enter image description here](https://i.imgur.com/O71cG5j.png) | ![enter image description here](https://i.imgur.com/JtbBgjS.png) | ![enter image description here](https://i.imgur.com/ABbuUIH.png%5B/img%5D) | ![enter image description here](https://i.imgur.com/76KNmta.png)| ![enter image description here](images/FICO.png)|
| --- | --- | --- | --- | --- | --- |
|  **Features** | **AWS** | **GCP** | **Azure** | **Databricks** | **FICO Platform** |
|  **Data pipeline** | [Data Pipeline](https://aws.amazon.com/datapipeline/) | [Dataflow](https://cloud.google.com/dataflow) | [Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/introduction) | Spark | Data Pipeline, DMP-S |
|  **Feature Store** | --- | --- | --- | --- | [Feature Store](https://www.fico.com/en/platform)|
|  **Model Monitoring** | [Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) | --- | [Azure Monitor](https://docs.microsoft.com/en-us/azure/machine-learning/monitor-azure-machine-learning) | --- | Decision Central |
|  **Experiment Management** | [SageMaker Experiments](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments.html#exp-mgmt-track) | --- | [Azure Machine Learning SDK](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow) | [MLFlow Tracking](https://www.mlflow.org/docs/latest/tracking.html) | --- |
|  **Model versioning** | [Production Variants](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-now-comes-with-new-capabilities-for-accelerating-machine-learning-experimentation/) | [Versions](https://cloud.google.com/ai-platform/training/docs/projects-models-versions-jobs) | [Model registration](https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment#register-package-and-deploy-models-from-anywhere) | [MLflow Model Registry](https://www.mlflow.org/docs/latest/model-registry.html) | --- |
|  **A/B Testing** | [Sagemaker](https://aws.amazon.com/blogs/machine-learning/a-b-testing-ml-models-in-production-using-amazon-sagemaker/) | --- | [Controlled Rollout](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-azure-kubernetes-service#deploy-models-to-aks-using-controlled-rollout-preview) | --- | --- |
|  **Model Serving** | [Sagemaker](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) | [AI Platform](https://cloud.google.com/ai-platform) | [Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where) | [MLFlow Model Serving](https://databricks.com/blog/2020/06/25/announcing-mlflow-model-serving-on-databricks.html) | [DMP](https://www.fico.com/en/platform)|
|  **AutoML**  [^2]| [Autopilot](https://aws.amazon.com/sagemaker/autopilot/) | [Cloud AutoML](https://cloud.google.com/automl) | [AutomatedML](https://azure.microsoft.com/en-us/services/machine-learning/automatedml/) | --- | Auto-RED[^1] |
|  **xAI**[^2]| --- | [What-if-tool](https://cloud.google.com/blog/products/ai-machine-learning/introducing-the-what-if-tool-for-cloud-ai-platform-models) | --- | --- | [xAI Tookit](https://www.fico.com/en/latest-thinking/white-paper/xai-toolkit-practical-explainable-machine-learning)  |
|  **Notebooks** | [Sagemaker Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) | [AI Platform Notebooks](https://cloud.google.com/ai-platform-notebooks) | [Microsoft Azure Notebooks](https://notebooks.azure.com/) | [Notebooks](https://docs.databricks.com/notebooks/index.html) | [Analytics Workbench](https://www.fico.com/en/products/fico-analytics-workbench) |
|  **Visual Scorecards & Decision Trees**[^2] | --- | --- | --- | --- | [Analytics Workbench](https://www.fico.com/en/products/fico-analytics-workbench) |
|  **Decisions**[^2] | --- | --- | --- | --- | [Decision Modeler](https://www.fico.com/en/products/fico-decision-modeler) |
|  **Constraint Programmning** [^2] | --- | [OR-Tools](https://developers.google.com/optimization/examples) | --- | --- | [Xpress](https://www.fico.com/en/products/optimization) |
|  **Linear and non-linear optimization** [^2] | --- | [OR-Tools](https://developers.google.com/optimization/examples) | --- | --- | [Xpress](https://www.fico.com/en/products/optimization) |
|  **Deployment Options** [^2] | Cloud SaaS Only | Cloud SaaS Only   | Cloud SaaS Only  | Cloud SaaS and Multi Cloud | Cloud SaaS, Multi Cloud, and On-premise |

This is based on a comparison described here: https://towardsdatascience.com/end-to-end-machine-learning-platforms-compared-c530d626151b

[^1]:Internal Alpha.

[^2]:Added by Jari.


