# Import the streamlit library
import streamlit as st

# Import the numpy and skimage libraries
import numpy as np
from skimage import io


# Cache the results of the function for 300 seconds
@st.cache_data(ttl=300)
# Define a function called "plot"
def plot():
    # Read in an image from the specified URL using skimage
    vol = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")
    # Transpose the image to create a 3D volume
    volume = vol.T
    # Get the dimensions of the volume
    r, c = volume[0].shape

    # Import the plotly.graph_objects library and define the number of frames
    import plotly.graph_objects as go
    nb_frames = 68

    # Create a new figure with frames
    fig = go.Figure(frames=[go.Frame(data=go.Surface(
        z=(6.7 - k * 0.1) * np.ones((r, c)),
        surfacecolor=np.flipud(volume[67 - k]),
        cmin=0, cmax=200
        ),
        name=str(k) # you need to name the frame for the animation to behave properly
        )
        for k in range(nb_frames)])

    # Add data to be displayed before animation starts
    fig.add_trace(go.Surface(
        z=6.7 * np.ones((r, c)),
        surfacecolor=np.flipud(volume[67]),
        colorscale='Gray',
        cmin=0, cmax=200,
        colorbar=dict(thickness=20, ticklen=4)
        ))

    # Define a function to set the frame arguments for the animation
    st.cache_data(ttl=300)
    def frame_args(duration):
        return {
                "frame": {"duration": duration},
                "mode": "immediate",
                "fromcurrent": True,
                "transition": {"duration": duration, "easing": "linear"},
            }

    # Create a slider for the animation
    sliders = [
                {
                    "pad": {"b": 10, "t": 60},
                    "len": 0.9,
                    "x": 0.1,
                    "y": 0,
                    "steps": [
                        {
                            "args": [[f.name], frame_args(0)],
                            "label": str(k),
                            "method": "animate",
                        }
                        for k, f in enumerate(fig.frames)
                    ],
                }
            ]

    # Define the layout of the plot
    fig.update_layout(
            title='Slices in volumetric data',
            width=600,
            height=600,
            scene=dict(
                        zaxis=dict(range=[-0.1, 6.8], autorange=False),
                        aspectratio=dict(x=1, y=1, z=1),
                        ),
            updatemenus = [
                {
                    "buttons": [
                        {
                            "args": [None, frame_args(50)],
                            "label": "&#9654;", # play symbol
                            "method": "animate",
                        },
                        {
                            "args": [[None], frame_args(0)],
                            "label": "&#9724;", # pause symbol
                            "method": "animate",
                        },
                    ],
                    "direction": "left",
                    "pad": {"r": 10, "t": 70},
                    "type": "buttons",
                    "x": 0.1,
                    "y": 0,
                }
            ],
            sliders=sliders
    )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)