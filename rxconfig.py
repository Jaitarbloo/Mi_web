import reflex as rx

config = rx.Config(
    app_name="Mi_web",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],

     api_url="https://jaitarbloo.onrender.com",
    
                   cors_allowed_origins=["http://localhost:3000",
        
                                        "https://mi-web-lime-eight.vercel.app",

                                          "https://www.jaitarbloo.com"
        
                                        ]
)