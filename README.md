# Black-Scholes-Merton Option Pricing Model with Streamlit: A Quantitative Finance Tool

This repository hosts a Python-based implementation of the seminal Black-Scholes-Merton (BSM) option pricing model, augmented with an intuitive web interface crafted using Streamlit. This tool empowers users to derive theoretical valuations for European-style vanilla options and analyze their sensitivities to key market parameters.

## Synopsis

The Black-Scholes-Merton model, a cornerstone of quantitative finance, provides a closed-form solution for pricing European options. This implementation furnishes a transparent and efficient means to compute option premiums based on critical market inputs. Leveraging the interactive capabilities of Streamlit, users can dynamically adjust these parameters and instantaneously observe the impact on option prices and their associated risk sensitivities, commonly known as the "Greeks."

## Key Features

* **Pricing of European Vanilla Options:** Computes the theoretical market value for both call and put options adhering to European exercise conventions.
* **Core BSM Formula Implementation:** Accurately implements the mathematical framework of the Black-Scholes-Merton model.
* **Computation of First-Order and Second-Order Greeks:** Calculates essential risk metrics:
    * **Delta ($\Delta$):** The first-order derivative of the option price with respect to the underlying asset's spot price, indicating the option's directional sensitivity.
    * **Gamma ($\Gamma$):** The second-order derivative of the option price with respect to the underlying asset's spot price, measuring the rate of change of delta. Crucial for hedging strategies involving dynamic adjustments.
    * **Theta ($\Theta$):** Measures the sensitivity of the option price to the passage of calendar time, often referred to as time decay. Expressed as the change in option price per unit of time.
    * **Vega ($\nu$):** Quantifies the option price's responsiveness to changes in the implied volatility of the underlying asset. A key metric for volatility trading.
    * **Rho ($\rho$):** Measures the sensitivity of the option price to fluctuations in the risk-free interest rate. Particularly relevant for longer-dated options.
* **Interactive Streamlit GUI:**
    * User-friendly widgets for inputting financial parameters.
    * Real-time recalculation and display of option prices and Greeks upon parameter modification.
    * Clear and concise presentation of valuation outputs and risk metrics.

## Technological Underpinnings

* **Python:** The foundational programming language employed for model implementation and application logic.
* **NumPy:** A fundamental package for numerical computing in Python, essential for array operations and mathematical functions, particularly the cumulative distribution function (CDF) of the standard normal distribution.
* **SciPy:** Provides advanced scientific computing routines, including the implementation of the cumulative standard normal distribution function (`scipy.stats.norm.cdf`), a critical component of the BSM formula.
* **Streamlit:** A powerful Python library for rapidly building and deploying interactive web applications, enabling the creation of the user interface for this option pricing tool.
