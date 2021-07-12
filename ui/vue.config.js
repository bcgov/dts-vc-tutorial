module.exports = {
  publicPath: "/static/ui/", // Should be STATIC_URL + path/to/build
  filenameHashing: false, // Django will hash file names, not webpack
  runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
  devServer: {
    writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    public: "http://localhost:8081/static/ui/",
  },
};
