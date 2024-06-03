import plotly.graph_objects as go


def plot_5_minute_mean(mean_5_minutes_year1, mean_5_minutes_year2,
                       start_date_year1, end_date_year1, start_date_year2, end_date_year2):
    """
    Plot the mean GHI for every 5 minutes for all specified years.
    """

    # Create a Plotly figure
    fig = go.Figure()

    # Convert the range object to a list for all years
    x_values_year1 = list(range(0, len(mean_5_minutes_year1) * 5, 5))
    x_values_year2 = list(range(0, len(mean_5_minutes_year2) * 5, 5))

    # Add traces for mean GHI for all years
    fig.add_trace(go.Scatter(x=x_values_year1,
                             y=mean_5_minutes_year1.values,
                             mode='lines+markers',
                             marker=dict(size=5),
                             line=dict(shape='linear', color='blue'),
                             name=2022))

    fig.add_trace(go.Scatter(x=x_values_year2,
                             y=mean_5_minutes_year2.values,
                             mode='lines+markers',
                             marker=dict(size=5),
                             line=dict(shape='linear', color='red'),
                             name=2020))

    # Update layout
    title = f'5 Minutes intervals mean from {start_date_year1.date()} to {end_date_year1.date()}, ' \
            f'{start_date_year2.date()} to {end_date_year2.date()}'

    fig.update_layout(title=title,
                      xaxis_title='Minutes',
                      yaxis_title='GHI (W/m2)',
                      xaxis=dict(tickvals=list(range(0, len(mean_5_minutes_year1) * 5, 60)),
                                 ticktext=[f'{i // 60:02d}:{i % 60:02d}h' for i in
                                           range(0, len(mean_5_minutes_year1) * 5, 60)]),
                      yaxis=dict(gridcolor='lightgray'),
                      template='plotly_white')

    # Show the plot
    fig.show()


def plot_hourly_energy_mean(hourly_energy, start_date, end_date, mean_daily_energy):
    """
    Plot the hourly mean of energy received within the specified date range.
    """
    # Calculate the mean energy received for each hour within the specified date range
    hourly_mean_energy = hourly_energy / ((end_date - start_date).days + 1)

    # Create a Plotly figure for the hourly mean energy
    fig = go.Figure()

    # Add a bar trace for the hourly mean energy
    fig.add_trace(go.Bar(x=hourly_mean_energy.index,
                         y=hourly_mean_energy.values,
                         name='Hourly Mean Energy'))

    # Update layout
    if start_date.date() == end_date.date():
        title = f'Hourly Mean Energy Received on {start_date.date()}, Mean Daily Energy: {mean_daily_energy:.2f} (Wh/m^2)'
    else:
        title = f'Hourly Mean Energy Received from {start_date.date()} to {end_date.date()}, ' \
                f'Mean Daily: {mean_daily_energy:.2f} (Wh/m^2)'
    fig.update_layout(title=title,
                      xaxis_title='Hour of Day',
                      yaxis_title='Energy Received (Wh/m^2)',
                      xaxis=dict(tickvals=list(range(24)),
                                 ticktext=[f'{i}:00' for i in range(24)]),
                      template='plotly_white')

    # Show the plot
    fig.show()


