FROM continuumio/miniconda3
RUN conda install --yes pytorch scikit-learn pandas numpy \
    && conda clean -afy

COPY . .
