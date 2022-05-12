from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class KieHttpParserConan(ConanFile):
    name = "kie_http_parser"
    version = "0.1.0"

    # Optional metadata
    license = "MIT"
    author = "Kie"
    url = "https://github.com/Kidsunbo/kie_http_parser"
    description = "An HTTP parser library"
    topics = ("HTTP", "Parser")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], 
                "fPIC": [True, False],
                "with_http1": [True, False],
                "with_http2": [True, False]
            }
    default_options = {"shared": False, "fPIC": True, "with_http1": True, "with_http2": False}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "http1/*", "http2/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        self.folders.build = "build"
        self.folders.generators = "build/generators"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["BUILD_HTTP1"] = self.options.with_http1
        tc.variables["BUILD_HTTP2"] = self.options.with_http2
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.a", "lib", "", keep_path=False)
        self.copy("*.lib", "lib", "", keep_path=False)
        if self.options.with_http1:
            self.copy("*.h", "include/http1", "http1/include")
            self.copy("*.hpp", "include/http1", "http1/include")
        if self.options.with_http2:
            self.copy("*.h", "include/http2", "http2/include")
            self.copy("*.hpp", "include/http2", "http2/include")


    def package_info(self):
        if self.options.with_http1:
            self.cpp_info.components["http1"].libs = ["http1"]
            self.cpp_info.components["http1"].libdirs = ["lib"]
            self.cpp_info.components["http1"].includedirs = ["include"]
        if self.options.with_http2:
            self.cpp_info.components["http2"].libs = ["http2"]
            self.cpp_info.components["http2"].libdirs = ["lib"]
            self.cpp_info.components["http2"].includedirs = ["include"]