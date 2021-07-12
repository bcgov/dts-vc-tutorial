module.exports = {
  // Should be STATIC_URL + path/to/build
  publicPath: "/static/ui/",

  // Django will hash file names, not webpack
  filenameHashing: false,

  // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
  runtimeCompiler: true,

  devServer: {
    writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    public: "http://localhost:8081/static/ui/",
  },

  transpileDependencies: ["vuetify"],
};
