import reflex as rx

config = rx.Config(
    app_name="Mi_web",
    html_lang="es",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],

     #api_url="https://mi-web-93ls.onrender.com", 
     api_url="http://localhost:8000",
                   
                   cors_allowed_origins=["http://localhost:3000",
        
                                        "https://mi-web-lime-eight.vercel.app",

                                          "https://www.jaitarbloo.com"
        
                                        ]
)