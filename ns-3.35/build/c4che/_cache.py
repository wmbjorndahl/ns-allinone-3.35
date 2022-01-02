APPNAME = 'ns'
AR = ['/usr/bin/ar']
ARCH_ST = ['-arch']
ARFLAGS = ['rcs']
BINDIR = '/usr/local/bin'
BUILD_PROFILE = 'debug'
BUILD_SUFFIX = '-debug'
CC = ['/usr/bin/clang']
CCDEFINES = ['_DEBUG']
CCFLAGS = ['-O0', '-ggdb', '-g3', '-Wall', '-Werror', '-O0', '-ggdb', '-g3', '-Wall', '-Werror', '-Wno-unused-local-typedefs', '-Wno-potentially-evaluated-expression', '-std=c++17']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'clang'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('13', '0', '0')
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_PYEMBED = ['-fno-common', '-dynamic', '-g', '-fwrapv', '-O3', '-isysroot', '/Library/Developer/CommandLineTools/SDKs/MacOSX12.sdk']
CFLAGS_PYEXT = ['-fno-common', '-dynamic', '-g', '-fwrapv', '-O3', '-isysroot', '/Library/Developer/CommandLineTools/SDKs/MacOSX12.sdk']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'clang'
COMPILER_CXX = 'clang++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/clang++']
CXXDEFINES = ['_DEBUG']
CXXFLAGS = ['-O0', '-ggdb', '-g3', '-Wall', '-Werror', '-Wno-unused-local-typedefs', '-Wno-potentially-evaluated-expression', '-std=c++17']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_PYEMBED = ['-fno-common', '-dynamic', '-g', '-fwrapv', '-O3', '-isysroot', '/Library/Developer/CommandLineTools/SDKs/MacOSX12.sdk']
CXXFLAGS_PYEXT = ['-fno-common', '-dynamic', '-g', '-fwrapv', '-O3', '-isysroot', '/Library/Developer/CommandLineTools/SDKs/MacOSX12.sdk', '-Wno-array-bounds']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'clang'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DATADIR = '/usr/local/share'
DATAROOTDIR = '/usr/local/share'
DEFINES = ['NS3_BUILD_PROFILE_DEBUG', 'NS3_ASSERT_ENABLE', 'NS3_LOG_ENABLE', 'HAVE_SYS_IOCTL_H=1', 'HAVE_IF_NETS_H=1', 'HAVE_NET_ETHERNET_H=1', 'HAVE_SQLITE3=1', 'HAVE_SEMAPHORE_H=1']
DEFINES_PYEMBED = ['NDEBUG']
DEFINES_PYEXT = ['NDEBUG']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'PYTHONDIR': '', 'PYTHONARCHDIR': '', 'HAVE_PYEMBED': '', 'HAVE_PYEXT': '', 'HAVE_PYTHON_H': '', 'HAVE_LIBXML2': '', 'HAVE_UINT128_T': '', 'HAVE___UINT128_T': '', 'INT64X64_USE_128': '', 'HAVE_STDINT_H': '', 'HAVE_INTTYPES_H': '', 'HAVE_SYS_INT_TYPES_H': '', 'HAVE_SYS_TYPES_H': '', 'HAVE_SYS_STAT_H': '', 'HAVE_DIRENT_H': '', 'HAVE_SIGNAL_H': '', 'HAVE_PTHREAD_H': '', 'HAVE_RT': '', 'HAVE_SYS_IOCTL_H': '', 'HAVE_IF_NETS_H': '', 'HAVE_NET_ETHERNET_H': '', 'HAVE_IF_TUN_H': '', 'HAVE_PACKET_H': '', 'HAVE_NETMAP_USER_H': '', 'HAVE_SQLITE3': '', 'HAVE_SEMAPHORE_H': ''}
DEST_BINFMT = 'mac-o'
DEST_CPU = 'aarch64'
DEST_OS = 'darwin'
DOCDIR = '/usr/local/share/doc/ns'
DVIDIR = '/usr/local/share/doc/ns'
ENABLE_BRITE = False
ENABLE_BUILD_VERSION = False
ENABLE_DPDKNETDEV = False
ENABLE_EMU = None
ENABLE_EXAMPLES = True
ENABLE_FDNETDEV = True
ENABLE_GSL = None
ENABLE_GTK = None
ENABLE_LIBXML2 = '-lxml2\n'
ENABLE_NETMAP_EMU = None
ENABLE_NSC = False
ENABLE_PYTHON_BINDINGS = True
ENABLE_PYVIZ = False
ENABLE_STATIC_NS3 = False
ENABLE_SUDO = False
ENABLE_TAP = None
ENABLE_TESTS = True
ENABLE_THREADING = True
EXAMPLE_DIRECTORIES = ['tutorial', 'udp', 'energy', 'matrix-topology', 'channel-models', 'realtime', 'tcp', 'wireless', 'naming', 'traffic-control', 'error-model', 'routing', 'ipv6', 'stats', 'socket', 'udp-client-server']
EXEC_PREFIX = '/usr/local'
FRAMEWORKPATH_ST = '-F%s'
FRAMEWORK_PYEMBED = ['CoreFoundation']
FRAMEWORK_PYEXT = ['CoreFoundation']
FRAMEWORK_ST = ['-framework']
GCC_RTTI_ABI_COMPLETE = 'False'
HAVE_DIRENT_H = 1
HAVE_INTTYPES_H = 1
HAVE_LIBXML2 = 1
HAVE_NET_ETHERNET_H = 1
HAVE_NET_IF_H = 1
HAVE_PTHREAD_H = 1
HAVE_PYEMBED = 1
HAVE_PYEXT = 1
HAVE_PYTHON_H = 1
HAVE_SEMAPHORE_H = 1
HAVE_SIGNAL_H = 1
HAVE_SQLITE3 = 1
HAVE_STDINT_H = 1
HAVE_SYS_IOCTL_H = 1
HAVE_SYS_STAT_H = 1
HAVE_SYS_TYPES_H = 1
HAVE___UINT128_T = 1
HTMLDIR = '/usr/local/share/doc/ns'
INCLUDEDIR = '/usr/local/include'
INCLUDES_PYEMBED = ['/opt/homebrew/opt/python@3.9/Frameworks/Python.framework/Versions/3.9/include/python3.9']
INCLUDES_PYEXT = ['/opt/homebrew/opt/python@3.9/Frameworks/Python.framework/Versions/3.9/include/python3.9']
INFODIR = '/usr/local/share/info'
INT64X64_USE_128 = 1
LIBDIR = '/usr/local/lib'
LIBEXECDIR = '/usr/local/libexec'
LIBPATH_PYEMBED = ['/opt/homebrew/opt/python@3.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/config-3.9-darwin']
LIBPATH_PYEXT = ['/opt/homebrew/opt/python@3.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/config-3.9-darwin']
LIBPATH_ST = '-L%s'
LIB_BOOST = []
LIB_LIBXML2 = ['xml2']
LIB_PYEMBED = ['python3.9', 'dl', 'python3.9', 'dl']
LIB_PYEXT = ['dl', 'dl']
LIB_SQLITE3 = ['sqlite3']
LIB_ST = '-l%s'
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_PYEMBED = []
LINKFLAGS_PYEXT = []
LINKFLAGS_cshlib = ['-dynamiclib']
LINKFLAGS_cstlib = []
LINKFLAGS_cxxshlib = ['-dynamiclib']
LINKFLAGS_cxxstlib = []
LINK_CC = ['/usr/bin/clang']
LINK_CXX = ['/usr/bin/clang++']
LOCALEDIR = '/usr/local/share/locale'
LOCALSTATEDIR = '/usr/local/var'
MACOSX_DEPLOYMENT_TARGET = '12'
MANDIR = '/usr/local/share/man'
MODULES_NOT_BUILT = ['brite', 'click', 'dpdk-net-device', 'mpi', 'openflow', 'tap-bridge', 'visualizer']
NS3_CONTRIBUTED_MODULES = []
NS3_ENABLED_CONTRIBUTED_MODULES = []
NS3_ENABLED_MODULES = ['ns3-antenna', 'ns3-aodv', 'ns3-applications', 'ns3-bridge', 'ns3-buildings', 'ns3-config-store', 'ns3-core', 'ns3-csma', 'ns3-csma-layout', 'ns3-dsdv', 'ns3-dsr', 'ns3-energy', 'ns3-fd-net-device', 'ns3-flow-monitor', 'ns3-internet', 'ns3-internet-apps', 'ns3-lr-wpan', 'ns3-lte', 'ns3-mesh', 'ns3-mobility', 'ns3-netanim', 'ns3-network', 'ns3-nix-vector-routing', 'ns3-olsr', 'ns3-point-to-point', 'ns3-point-to-point-layout', 'ns3-propagation', 'ns3-sixlowpan', 'ns3-spectrum', 'ns3-stats', 'ns3-test', 'ns3-topology-read', 'ns3-traffic-control', 'ns3-uan', 'ns3-virtual-net-device', 'ns3-wave', 'ns3-wifi', 'ns3-wimax']
NS3_EXECUTABLE_PATH = ['/Users/william/Documents/ns-allinone-3.35/ns-3.35/build/src/fd-net-device']
NS3_MODULES = ['ns3-antenna', 'ns3-aodv', 'ns3-applications', 'ns3-bridge', 'ns3-buildings', 'ns3-config-store', 'ns3-core', 'ns3-csma', 'ns3-csma-layout', 'ns3-dsdv', 'ns3-dsr', 'ns3-energy', 'ns3-fd-net-device', 'ns3-flow-monitor', 'ns3-internet', 'ns3-internet-apps', 'ns3-lr-wpan', 'ns3-lte', 'ns3-mesh', 'ns3-mobility', 'ns3-netanim', 'ns3-network', 'ns3-nix-vector-routing', 'ns3-olsr', 'ns3-point-to-point', 'ns3-point-to-point-layout', 'ns3-propagation', 'ns3-sixlowpan', 'ns3-spectrum', 'ns3-stats', 'ns3-test', 'ns3-topology-read', 'ns3-traffic-control', 'ns3-uan', 'ns3-virtual-net-device', 'ns3-wave', 'ns3-wifi', 'ns3-wimax']
NS3_MODULE_PATH = ['/Users/william/Documents/ns-allinone-3.35/ns-3.35/build/lib', '/Users/william/Documents/ns-allinone-3.35/ns-3.35/build']
NS3_OPTIONAL_FEATURES = [('python', 'Python Bindings', True, None), ('castxml', 'Python API Scanning Support', False, "Missing 'pygccxml' Python module"), ('brite', 'BRITE Integration', False, 'BRITE not enabled (see option --with-brite)'), ('nsclick', 'NS-3 Click Integration', False, 'nsclick not enabled (see option --with-nsclick)'), ('GtkConfigStore', 'GtkConfigStore', [], "library 'gtk+-3 >= 3.22' not found"), ('XmlIo', 'XmlIo', '-lxml2\n', "library 'libxml-2.0 >= 2.7' not found"), ('Threading', 'Threading Primitives', True, '<pthread.h> include not detected'), ('RealTime', 'Real Time Simulator', False, 'librt is not available'), ('FdNetDevice', 'File descriptor NetDevice', True, 'FdNetDevice module enabled'), ('DpdkNetDevice', 'DPDK NetDevice', False, 'libdpdk not found, $RTE_SDK and/or $RTE_TARGET environment variable not set or incorrect'), ('TapFdNetDevice', 'Tap FdNetDevice', False, 'needs linux/if_tun.h'), ('EmuFdNetDevice', 'Emulation FdNetDevice', False, 'needs netpacket/packet.h'), ('NetmapFdNetDevice', 'Netmap emulation FdNetDevice', False, 'needs net/netmap_user.h'), ('PlanetLabFdNetDevice', 'PlanetLab FdNetDevice', False, 'PlanetLab operating system not detected (see option --force-planetlab)'), ('nsc', 'Network Simulation Cradle', False, 'NSC not found (see option --with-nsc)'), ('mpi', 'MPI Support', False, 'option --enable-mpi not selected'), ('openflow', 'NS-3 OpenFlow Integration', False, 'OpenFlow not enabled (see option --with-openflow)'), ('SQLiteStats', 'SQLite stats support', True, "library 'sqlite3' and/or semaphore.h not found"), ('TapBridge', 'Tap Bridge', [], '<linux/if_tun.h> include not detected'), ('PyViz', 'PyViz visualizer', False, 'Missing python modules: gi, gi.repository.GObject, cairo, pygraphviz, gi.repository.Gtk, gi.repository.Gdk, gi.repository.Pango, gi.repository.GooCanvas'), ('ENABLE_SUDO', 'Use sudo to set suid bit', False, 'option --enable-sudo not selected'), ('ENABLE_TESTS', 'Tests', True, 'option --enable-tests selected'), ('ENABLE_EXAMPLES', 'Examples', True, 'option --enable-examples selected'), ('GSL', 'GNU Scientific Library (GSL)', [], 'GSL not found'), ('libgcrypt', 'Gcrypt library', [], 'libgcrypt not found: you can use libgcrypt-config to find its location.'), ('DES Metrics', 'DES Metrics event collection', [], 'defaults to disabled')]
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'ns'
PDFDIR = '/usr/local/share/doc/ns'
PKGCONFIG = ['/opt/homebrew/bin/pkg-config']
PLATFORM = 'darwin'
PREFIX = '/usr/local'
PRINT_BUILT_MODULES_AT_END = False
PSDIR = '/usr/local/share/doc/ns'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTAG = 'cpython-39'
PYTHON = ['/opt/homebrew/opt/python@3.9/bin/python3.9']
PYTHONARCHDIR = '/usr/local/lib/python3.9/site-packages'
PYTHONDIR = '/usr/local/lib/python3.9/site-packages'
PYTHON_BINDINGS_APIDEFS = 'gcc-ILP32'
PYTHON_CONFIG = ['/opt/homebrew/opt/python@3.9/bin/python3.9-config']
PYTHON_VERSION = '3.9'
REQUIRED_BOOST_LIBS = []
RPATH_ST = '-Wl,-rpath,%s'
SBINDIR = '/usr/local/sbin'
SEMAPHORE_ENABLED = True
SHAREDSTATEDIR = '/usr/local/com'
SHLIB_MARKER = []
SONAME_ST = []
SQLITE_STATS = '-lsqlite3\n'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = []
STLIB_ST = '-l%s'
SUDO = ['/usr/bin/sudo']
SYSCONFDIR = '/usr/local/etc'
VALGRIND_FOUND = False
VERSION = '3.35'
WITH_PYBINDGEN = '/Users/william/Documents/ns-allinone-3.35/pybindgen-0.22.0'
cfg_files = ['/Users/william/Documents/ns-allinone-3.35/ns-3.35/build/ns3/config-store-config.h', '/Users/william/Documents/ns-allinone-3.35/ns-3.35/build/ns3/core-config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.dylib'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.dylib'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_SYS_IOCTL_H', 'HAVE_IF_NETS_H', 'HAVE_NET_ETHERNET_H', 'HAVE_IF_TUN_H', 'HAVE_PACKET_H', 'HAVE_NETMAP_USER_H', 'HAVE_SQLITE3', 'HAVE_SEMAPHORE_H']
macbundle_PATTERN = '%s.bundle'
pyext_PATTERN = '%s.cpython-39-darwin.so'
