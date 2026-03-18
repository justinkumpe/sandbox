# Use nginx alpine for a lightweight web server
FROM nginx:1.27-alpine

# Copy the HTML file to nginx's default serving directory
COPY index.html /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# nginx will automatically start and serve the content
CMD ["nginx", "-g", "daemon off;"]
