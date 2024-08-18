import pandas as pd


def calculate_dates_mean_ghi(df, start_date, end_date):
    """
    Calculate hourly mean GHI (Global Horizontal Irradiance) for each hour between the given date range.
    """

    # Increment end_date by one day to make the range inclusive
    end_date_inclusive = pd.to_datetime(end_date) + pd.DateOffset(days=1)

    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] < end_date_inclusive)]

    # Group the data by 5-minute intervals and calculate the mean GHI for each group
    mean_ghi_5min = filtered_df.groupby(filtered_df['Date'].dt.time)['ghi'].mean()

    return mean_ghi_5min


def calculate_hourly_energy(df, start_date, end_date):
    """
    Calculate hourly energy (total energy received) in Wh/m^2 within the specified date range.
    """
    end_date_inclusive = pd.to_datetime(end_date) + pd.DateOffset(days=1)
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] < end_date_inclusive)]

    # Extract hour from the datetime column
    filtered_df = filtered_df.assign(hour=filtered_df['Date'].dt.hour)
    # Group the data by hour and calculate the total energy received (sum of GHI) for each group
    hourly_energy = filtered_df.groupby('hour')['ghi'].sum()
    hourly_energy = hourly_energy / 12
    return hourly_energy


def calculate_mean_daily_energy(df, start_date, end_date):
    """
    Calculate the mean daily energy (total energy received) in Wh/m^2 within the specified date range.
    """
    daily_energy = calculate_daily_energy(df, start_date, end_date)
    mean_daily_energy = daily_energy.mean()
    # Format mean_daily_energy to 2 decimal points
    formatted_mean_daily_energy = f"{mean_daily_energy:.2f}"
    return formatted_mean_daily_energy


def calculate_daily_energy(df, start_date, end_date):
    """
    Calculate daily energy (total energy received) in Wh/m^2 within the specified date range.
    """
    end_date_inclusive = pd.to_datetime(end_date) + pd.DateOffset(days=1)
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] < end_date_inclusive)].copy()

    # Extract date from the datetime column
    filtered_df['date'] = filtered_df['Date'].dt.date

    # Group the data by date and calculate the total energy received (sum of GHI) for each group
    daily_energy = filtered_df.groupby('date')['ghi'].sum()
    return daily_energy / 12


