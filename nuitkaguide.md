

### How to compile your python file to exe?

Try using nuitka module.


<pre><code class="has-line-data" data-line-start="71" data-line-end="75" class="language-sh">pip install nuitka <span class="hljs-comment"># default module for compilling (!)</span>
pip install zstandard <span class="hljs-comment"># onefile mode (required if you use --onefile argument)</span>
pip install orderedset <span class="hljs-comment"># module for good optimization and fast compilling (*)</span>
</code></pre>

example for terminal: <pre><code class="has-line-data" data-line-start="1" data-line-end="3" class="language-sh">nuitka &lt;arguments&gt; &lt;script_name&gt; </code></pre> 

</span>
</code></pre>
<pre><code class="has-line-data" data-line-start="76" data-line-end="593" class="language-sh">Options:
  --version             show program<span class="hljs-string">'s version number and exit
  -h, --help            show this help message and exit
  --module              Create an extension module executable instead of a
                        program. Defaults to off.
  --standalone          Enable standalone mode for output. This allows you to
                        transfer the created binary to other machines without
                        it using an existing Python installation. This also
                        means it will become big. It implies these option: "--
                        follow-imports" and "--python-flag=no_site". Defaults
                        to off.
  --onefile             On top of standalone mode, enable onefile mode. This
                        means not a folder, but a compressed executable is
                        created and used. Defaults to off.
  --python-debug        Use debug version or not. Default uses what you are
                        using to run Nuitka, most likely a non-debug version.
  --python-flag=FLAG    Python flags to use. Default is what you are using to
                        run Nuitka, this enforces a specific mode. These are
                        options that also exist to standard Python executable.
                        Currently supported: "-S" (alias "no_site"),
                        "static_hashes" (do not use hash randomization),
                        "no_warnings" (do not give Python runtime warnings),
                        "-O" (alias "no_asserts"), "no_docstrings" (do not use
                        doc strings), "-u" (alias "unbuffered") and "-m".
                        Default empty.
  --python-for-scons=PATH
                        If using Python3.3 or Python3.4, provide the path of a
                        Python binary to use for Scons. Otherwise Nuitka can
                        use what you run Nuitka with or a Python installation
                        from Windows registry. On Windows Python 3.5 or higher
                        is needed. On non-Windows, Python 2.6 or 2.7 will do
                        as well.

  Control the warnings to be given by Nuitka:
    --warn-implicit-exceptions
                        Enable warnings for implicit exceptions detected at
                        compile time.
    --warn-unusual-code
                        Enable warnings for unusual code detected at compile
                        time.
    --assume-yes-for-downloads
                        Allow Nuitka to download external code if necessary,
                        e.g. dependency walker, ccache, and even gcc on
                        Windows. To disable, redirect input from nul device,
                        e.g. "&lt;/dev/null" or "&lt;NUL:". Default is to prompt.
    --nowarn-mnemonic=MNEMONIC
                        Disable warning for a given mnemonic. These are given
                        to make sure you are aware of certain topics, and
                        typically point to the Nuitka website. The mnemonic is
                        the part of the URL at the end, without the HTML
                        suffix. Can be given multiple times and accepts shell
                        pattern. Default empty.

  Control the inclusion of modules and packages in result:
    --include-package=PACKAGE
                        Include a whole package. Give as a Python namespace,
                        e.g. "some_package.sub_package" and Nuitka will then
                        find it and include it and all the modules found below
                        that disk location in the binary or extension module
                        it creates, and make it available for import by the
                        code. To avoid unwanted sub packages, e.g. tests you
                        can e.g. do this "--nofollow-import-to=*.tests".
                        Default empty.
    --include-module=MODULE
                        Include a single module. Give as a Python namespace,
                        e.g. "some_package.some_module" and Nuitka will then
                        find it and include it in the binary or extension
                        module it creates, and make it available for import by
                        the code. Default empty.
    --include-plugin-directory=MODULE/PACKAGE
                        Include also the code found in that directory,
                        considering as if they are each given as a main file.
                        Overrides all other inclusion options. You ought to
                        prefer other inclusion options, that go by names,
                        rather than filenames, as this always includes too
                        much, and find things through being in "sys.path". Can
                        be given multiple times. Default empty.
    --include-plugin-files=PATTERN
                        Include into files matching the PATTERN. Overrides all
                        other follow options. Can be given multiple times.
                        Default empty.
    --prefer-source-code
                        For already compiled extension modules, where there is
                        both a source file and an extension module, normally
                        the extension module is used, but it should be better
                        to compile the module from available source code for
                        best performance. If not desired, there is --no-
                        prefer-source-code to disable warnings about it.
                        Default off.

  Control the following into imported modules:
    --follow-stdlib     Also descend into imported modules from standard
                        library. This will increase the compilation time by a
                        lot. Defaults to off.
    --nofollow-imports  When --nofollow-imports is used, do not descend into
                        any imported modules at all, overrides all other
                        inclusion options. Defaults to off.
    --follow-imports    When --follow-imports is used, attempt to descend into
                        all imported modules. Defaults to off.
    --follow-import-to=MODULE/PACKAGE
                        Follow to that module if used, or if a package, to the
                        whole package. Can be given multiple times. Default
                        empty.
    --nofollow-import-to=MODULE/PACKAGE
                        Do not follow to that module name even if used, or if
                        a package name, to the whole package in any case,
                        overrides all other options. Can be given multiple
                        times. Default empty.

  Data files:
    --include-package-data=PACKAGE
                        Include data files of the given package name. Can use
                        patterns. By default Nuitka does not unless hard coded
                        and vital for operation of a package. This will
                        include all non-DLL, non-extension modules in the
                        distribution. Default empty.
    --include-data-files=DESC
                        Include data files by filenames in the distribution.
                        There are many allowed forms. With '</span>--include-data-
                        files=/path/to/file/*.txt=folder_name/some.txt<span class="hljs-string">' it
                        will copy a single file and complain if it'</span>s multiple.
                        With <span class="hljs-string">'--include-data-
                        files=/path/to/files/*.txt=folder_name/'</span> it will put
                        all matching files into that folder. For recursive
                        copy there is a form with <span class="hljs-number">3</span> values that <span class="hljs-string">'--include-
                        data-files=/path/to/scan=folder_name=**/*.txt'</span> that
                        will preserve directory structure. Default empty.
    --include-data-dir=DIRECTORY
                        Include data files from complete directory <span class="hljs-keyword">in</span> the
                        distribution. This is recursive. Check <span class="hljs-string">'--include-
                        data-files'</span> with patterns <span class="hljs-keyword">if</span> you want non-recursive
                        inclusion. An example would be <span class="hljs-string">'--include-data-
                        dir=/path/some_dir=data/some_dir'</span> <span class="hljs-keyword">for</span> plain copy, of
                        the whole directory. All files are copied, <span class="hljs-keyword">if</span> you want
                        to exclude files you need to remove them beforehand,
                        or use <span class="hljs-string">'--noinclude-data-files'</span> option to remove them.
                        Default empty.
    --noinclude-data-files=PATTERN
                        Do not include data files matching the filename
                        pattern given. This is against the target filename,
                        not <span class="hljs-built_in">source</span> paths. So ignore file pattern from package
                        data <span class="hljs-keyword">for</span> <span class="hljs-string">"package_name"</span> should be matched as
                        <span class="hljs-string">"package_name/*.txt"</span>. Default empty.

  DLL files:
    --noinclude-dlls=PATTERN
                        Do not include DLL files matching the filename pattern
                        given. This is against the target filename, not <span class="hljs-built_in">source</span>
                        paths. So ignore a DLL <span class="hljs-string">"someDLL"</span> contained <span class="hljs-keyword">in</span> the
                        package <span class="hljs-string">"package_name"</span> it should be matched as
                        <span class="hljs-string">"package_name/someDLL.*"</span>. Default empty.

  Immediate execution after compilation:
    --run               Execute immediately the created binary (or import the
                        compiled module). Defaults to off.
    --debugger, --gdb   Execute inside a debugger, e.g. <span class="hljs-string">"gdb"</span> or <span class="hljs-string">"lldb"</span> to
                        automatically get a stack trace. Defaults to off.
    --execute-with-pythonpath
                        When immediately executing the created binary (<span class="hljs-string">'--
                        execute'</span>), don<span class="hljs-string">'t reset '</span>PYTHONPATH<span class="hljs-string">' environment. When
                        all modules are successfully included, you ought to
                        not need PYTHONPATH anymore.

  Dump options for internal tree:
    --xml               Dump the final result of optimization as XML, then
                        exit.

  Compilation choices:
    --user-package-configuration-file=USER_YAML
                        User provided Yaml file with package configuration.
                        You can include DLLs, remove bloat, add hidden
                        dependencies. Check User Manual for a complete
                        description of the format to use. Can be given
                        multiple times. Defaults to empty.
    --disable-bytecode-cache
                        Do not reuse dependency analysis results for modules,
                        esp. from standard library, that are included as
                        bytecode.
    --full-compat       Enforce absolute compatibility with CPython. Do not
                        even allow minor deviations from CPython behavior,
                        e.g. not having better tracebacks or exception
                        messages which are not really incompatible, but only
                        different or worse. This is intended for tests only
                        and should *not* be used.
    --file-reference-choice=MODE
                        Select what value "__file__" is going to be. With
                        "runtime" (default for standalone binary mode and
                        module mode), the created binaries and modules, use
                        the location of themselves to deduct the value of
                        "__file__". Included packages pretend to be in
                        directories below that location. This allows you to
                        include data files in deployments. If you merely seek
                        acceleration, it'</span>s better <span class="hljs-keyword">for</span> you to use the
                        <span class="hljs-string">"original"</span> value, <span class="hljs-built_in">where</span> the <span class="hljs-built_in">source</span> files location will
                        be used. With <span class="hljs-string">"frozen"</span> a notation <span class="hljs-string">"&lt;frozen
                        module_name&gt;"</span> is used. For compatibility reasons, the
                        <span class="hljs-string">"__file__"</span> value will always have <span class="hljs-string">".py"</span> suffix
                        independent of what it really is.
    --module-name-choice=MODE
                        Select what value <span class="hljs-string">"__name__"</span> and <span class="hljs-string">"__package__"</span> are
                        going to be. With <span class="hljs-string">"runtime"</span> (default <span class="hljs-keyword">for</span> module mode),
                        the created module uses the parent package to deduce
                        the value of <span class="hljs-string">"__package__"</span>, to be fully compatible.
                        The value <span class="hljs-string">"original"</span> (default <span class="hljs-keyword">for</span> other modes) allows
                        <span class="hljs-keyword">for</span> more static optimization to happen, but is
                        incompatible <span class="hljs-keyword">for</span> modules that normally can be loaded
                        into any package.

  Output choices:
    -o FILENAME         Specify how the executable should be named. For
                        extension modules there is no choice, also not <span class="hljs-keyword">for</span>
                        standalone mode and using it will be an error. This
                        may include path information that needs to exist
                        though. Defaults to <span class="hljs-string">'&lt;program_name&gt;'</span> on this platform.
                        .exe
    --output-dir=DIRECTORY
                        Specify <span class="hljs-built_in">where</span> intermediate and final output files
                        should be put. The DIRECTORY will be populated with C
                        files, object files, etc. Defaults to current
                        directory.
    --remove-output     Removes the build directory after producing the module
                        or exe file. Defaults to off.
    --no-pyi-file       Do not create a <span class="hljs-string">".pyi"</span> file <span class="hljs-keyword">for</span> extension modules
                        created by Nuitka. This is used to detect implicit
                        imports. Defaults to off.

  Debug features:
    --debug             Executing all self checks possible to find errors <span class="hljs-keyword">in</span>
                        Nuitka, <span class="hljs-keyword">do</span> not use <span class="hljs-keyword">for</span> production. Defaults to off.
    --unstriped         Keep debug info <span class="hljs-keyword">in</span> the resulting object file <span class="hljs-keyword">for</span>
                        better debugger interaction. Defaults to off.
    --profile           Enable vmprof based profiling of time spent. Not
                        working currently. Defaults to off.
    --internal-graph    Create graph of optimization process internals, <span class="hljs-keyword">do</span> not
                        use <span class="hljs-keyword">for</span> whole programs, but only <span class="hljs-keyword">for</span> small <span class="hljs-built_in">test</span> cases.
                        Defaults to off.
    --trace-execution   Traced execution output, output the line of code
                        before executing it. Defaults to off.
    --recompile-c-only  This is not incremental compilation, but <span class="hljs-keyword">for</span> Nuitka
                        development only. Takes existing files and simply
                        compile them as C again. Allows compiling edited C
                        files <span class="hljs-keyword">for</span> quick debugging changes to the generated
                        <span class="hljs-built_in">source</span>, e.g. to see <span class="hljs-keyword">if</span> code is passed by, values
                        output, etc, Defaults to off. Depends on compiling
                        Python <span class="hljs-built_in">source</span> to determine <span class="hljs-built_in">which</span> files it should look
                        at.
    --generate-c-only   Generate only C <span class="hljs-built_in">source</span> code, and <span class="hljs-keyword">do</span> not compile it to
                        binary or module. This is <span class="hljs-keyword">for</span> debugging and code
                        coverage analysis that doesn<span class="hljs-string">'t waste CPU. Defaults to
                        off. Do not think you can use this directly.
    --experimental=FLAG
                        Use features declared as '</span>experimental<span class="hljs-string">'. May have no
                        effect if no experimental features are present in the
                        code. Uses secret tags (check source) per experimented
                        feature.
    --low-memory        Attempt to use less memory, by forking less C
                        compilation jobs and using options that use less
                        memory. For use on embedded machines. Use this in case
                        of out of memory problems. Defaults to off.
    --disable-dll-dependency-cache
                        Disable the dependency walker cache. Will result in
                        much longer times to create the distribution folder,
                        but might be used in case the cache is suspect to
                        cause errors.
    --force-dll-dependency-cache-update
                        For an update of the dependency walker cache. Will
                        result in much longer times to create the distribution
                        folder, but might be used in case the cache is suspect
                        to cause errors or known to need an update.

  Backend C compiler choice:
    --clang             Enforce the use of clang. On Windows this requires a
                        working Visual Studio version to piggy back on.
                        Defaults to off.
    --mingw64           Enforce the use of MinGW64 on Windows. Defaults to
                        off.
    --msvc=MSVC_VERSION
                        Enforce the use of specific MSVC version on Windows.
                        Allowed values are e.g. "14.3" (MSVC 2022) and other
                        MSVC version numbers, specify "list" for a list of
                        installed compilers, or use "latest".  Defaults to
                        latest MSVC being used if installed, otherwise MinGW64
                        is used.
    -j N, --jobs=N      Specify the allowed number of parallel C compiler
                        jobs. Defaults to the system CPU count.
    --lto=choice        Use link time optimizations (MSVC, gcc, clang).
                        Allowed values are "yes", "no", and "auto" (when it'</span>s
                        known to work). Defaults to <span class="hljs-string">"auto"</span>.
    --static-libpython=choice
                        Use static link library of Python. Allowed values are
                        <span class="hljs-string">"yes"</span>, <span class="hljs-string">"no"</span>, and <span class="hljs-string">"auto"</span> (when it<span class="hljs-string">'s known to work).
                        Defaults to "auto".
    --disable-ccache    Do not attempt to use ccache (gcc, clang, etc.) or
                        clcache (MSVC, clangcl).

  PGO compilation choices:
    --pgo               Enables C level profile guided optimization (PGO), by
                        executing a dedicated build first for a profiling run,
                        and then using the result to feedback into the C
                        compilation. Note: This is experimental and not
                        working with standalone modes of Nuitka yet. Defaults
                        to off.
    --pgo-args=PGO_ARGS
                        Arguments to be passed in case of profile guided
                        optimization. These are passed to the special built
                        executable during the PGO profiling run. Default
                        empty.
    --pgo-executable=PGO_EXECUTABLE
                        Command to execute when collecting profile
                        information. Use this only, if you need to launch it
                        through a script that prepares it to run. Default use
                        created program.

  Tracing features:
    --quiet             Disable all information outputs, but show warnings.
                        Defaults to off.
    --show-scons        Operate Scons in non-quiet mode, showing the executed
                        commands. Defaults to off.
    --show-progress     Provide progress information and statistics. Defaults
                        to off.
    --no-progressbar    Disable progress bar. Defaults to off.
    --show-memory       Provide memory information and statistics. Defaults to
                        off.
    --show-modules      Provide information for included modules and DLLs
                        Defaults to off.
    --show-modules-output=PATH
                        Where to output --show-modules, should be a filename.
                        Default is standard output.
    --report=COMPILATION_REPORT_FILENAME
                        Report module inclusion in an XML output file. Default
                        is off.
    --verbose           Output details of actions taken, esp. in
                        optimizations. Can become a lot. Defaults to off.
    --verbose-output=PATH
                        Where to output --verbose, should be a filename.
                        Default is standard output.

  General OS controls:
    --disable-console, --macos-disable-console, --windows-disable-console
                        When compiling for Windows or macOS, disable the
                        console window and create a GUI application. Defaults
                        to off.
    --enable-console    When compiling for Windows or macOS, enable the
                        console window and create a console application. This
                        disables hints from certain modules, e.g. "PySide"
                        that suggest to disable it. Defaults to true.
    --force-stdout-spec=FORCE_STDOUT_SPEC, --windows-force-stdout-spec=FORCE_STDOUT_SPEC
                        Force standard output of the program to go to this
                        location. Useful for programs with disabled console
                        and programs using the Windows Services Plugin of
                        Nuitka commercial. Defaults to not active, use e.g.
                        '</span>%PROGRAM%.out.txt<span class="hljs-string">', i.e. file near your program.
    --force-stderr-spec=FORCE_STDERR_SPEC, --windows-force-stderr-spec=FORCE_STDERR_SPEC
                        Force standard error of the program to go to this
                        location. Useful for programs with disabled console
                        and programs using the Windows Services Plugin of
                        Nuitka commercial. Defaults to not active, use e.g.
                        '</span>%PROGRAM%.err.txt<span class="hljs-string">', i.e. file near your program.

  Windows specific controls:
    --windows-icon-from-ico=ICON_PATH
                        Add executable icon. Can be given multiple times for
                        different resolutions or files with multiple icons
                        inside. In the later case, you may also suffix with
                        #&lt;n&gt; where n is an integer index starting from 1,
                        specifying a specific icon to be included, and all
                        others to be ignored.
    --windows-icon-from-exe=ICON_EXE_PATH
                        Copy executable icons from this existing executable
                        (Windows only).
    --onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE
                        When compiling for Windows and onefile, show this
                        while loading the application. Defaults to off.
    --windows-uac-admin
                        Request Windows User Control, to grant admin rights on
                        execution. (Windows only). Defaults to off.
    --windows-uac-uiaccess
                        Request Windows User Control, to enforce running from
                        a few folders only, remote desktop access. (Windows
                        only). Defaults to off.
    --windows-company-name=WINDOWS_COMPANY_NAME
                        Name of the company to use in Windows Version
                        information.  One of file or product version is
                        required, when a version resource needs to be added,
                        e.g. to specify product name, or company name.
                        Defaults to unused.
    --windows-product-name=WINDOWS_PRODUCT_NAME
                        Name of the product to use in Windows Version
                        information. Defaults to base filename of the binary.
    --windows-file-version=WINDOWS_FILE_VERSION
                        File version to use in Windows Version information.
                        Must be a sequence of up to 4 numbers, e.g. 1.0.0.0,
                        only this format is allowed. One of file or product
                        version is required, when a version resource needs to
                        be added, e.g. to specify product name, or company
                        name. Defaults to unused.
    --windows-product-version=WINDOWS_PRODUCT_VERSION
                        Product version to use in Windows Version information.
                        Must be a sequence of up to 4 numbers, e.g. 1.0.0.0,
                        only this format is allowed. One of file or product
                        version is required, when a version resource needs to
                        be added, e.g. to specify product name, or company
                        name. Defaults to unused.
    --windows-file-description=WINDOWS_FILE_DESCRIPTION
                        Description of the file use in Windows Version
                        information.  One of file or product version is
                        required, when a version resource needs to be added,
                        e.g. to specify product name, or company name.
                        Defaults to nonsense.
    --onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC
                        Use this as a temporary folder. Defaults to
                        '</span>%TEMP%\onefile_%PID%_%TIME%<span class="hljs-string">', i.e. system temporary
                        directory.

  macOS specific controls:
    --macos-target-arch=MACOS_TARGET_ARCH
                        What architectures is this to supposed to run on.
                        Default and limit is what the running Python allows
                        for. Default is "native" which is the architecture the
                        Python is run with.
    --macos-create-app-bundle
                        When compiling for macOS, create a bundle rather than
                        a plain binary application. Currently experimental and
                        incomplete. Currently this is the only way to unlock
                        disabling of console.Defaults to off.
    --macos-app-icon=ICON_PATH
                        Add icon for the application bundle to use. Can be
                        given only one time. Defaults to Python icon if
                        available.
    --macos-signed-app-name=MACOS_SIGNED_APP_NAME
                        Name of the application to use for macOS signing.
                        Follow "com.YourCompany.AppName" naming results for
                        best results, as these have to be globally unique, and
                        will potentially grant protected API accesses.
    --macos-app-name=MACOS_APP_NAME
                        Name of the product to use in macOS bundle
                        information. Defaults to base filename of the binary.
    --macos-sign-identity=MACOS_APP_VERSION
                        When signing on macOS, by default an ad-hoc identify
                        will be used, but with this option your get to specify
                        another identity to use. The signing of code is now
                        mandatory on macOS and cannot be disabled. Default "-"
                        if not given, which means ad-hoc.
    --macos-app-version=MACOS_APP_VERSION
                        Product version to use in macOS bundle information.
                        Defaults to "1.0" if not given.
    --macos-app-protected-resource=RESOURCE_DESC
                        Request access for macOS protected resources, e.g.
                        "NSMicrophoneUsageDescription:Microphone access for
                        recording audio." requests access to the microphone
                        and provides an informative text for the user, why
                        that is needed. Before the colon, is an OS identifier
                        for an access right, then the informative text. Legal
                        values can be found on https://developer.apple.com/doc
                        umentation/bundleresources/information_property_list/p
                        rotected_resources and the option can be specified
                        multiple times. Default empty.

  Linux specific controls:
    --linux-icon=ICON_PATH, --linux-onefile-icon=ICON_PATH
                        Add executable icon for onefile binary to use. Can be
                        given only one time. Defaults to Python icon if
                        available.

  Plugin control:
    --enable-plugin=PLUGIN_NAME, --plugin-enable=PLUGIN_NAME
                        Enabled plugins. Must be plug-in names. Use --plugin-
                        list to query the full list and exit. Default empty.
    --disable-plugin=PLUGIN_NAME, --plugin-disable=PLUGIN_NAME
                        Disabled plugins. Must be plug-in names. Use --plugin-
                        list to query the full list and exit. Default empty.
    --plugin-no-detection
                        Plugins can detect if they might be used, and the you
                        can disable the warning via "--disable-plugin=plugin-
                        that-warned", or you can use this option to disable
                        the mechanism entirely, which also speeds up
                        compilation slightly of course as this detection code
                        is run in vain once you are certain of which plugins
                        to use. Defaults to off.
    --plugin-list       Show list of all available plugins and exit. Defaults
                        to off.
    --user-plugin=PATH  The file name of user plugin. Can be given multiple
                        times. Default empty.
    --show-source-changes
                        Show source changes to original Python file content
                        before compilation. Mostly intended for developing
                        plugins. Default False.

  Plugin anti-bloat:
    --show-anti-bloat-changes
                        Annotate what changes are by the plugin done.
    --noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE
                        What to do if a '</span>setuptools<span class="hljs-string">' or import is encountered.
                        This package can be big with dependencies, and should
                        definitely be avoided. Also handles '</span>setuptools_scm<span class="hljs-string">'.
    --noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE
                        What to do if a '</span>pytest<span class="hljs-string">' import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided. Also handles '</span>nose<span class="hljs-string">' imports.
    --noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE
                        What to do if a unittest import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE
                        What to do if a IPython import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-default-mode=NOINCLUDE_DEFAULT_MODE
                        This actually provides the default "warning" value for
                        above options, and can be used to turn all of these
                        on.
    --noinclude-custom-mode=CUSTOM_CHOICES
                        What to do if a specific import is encountered. Format
                        is module name, which can and should be a top level
                        package and then one choice, "error", "warning",
                        "nofollow", e.g. PyQt5:error.
</span></code></pre>
