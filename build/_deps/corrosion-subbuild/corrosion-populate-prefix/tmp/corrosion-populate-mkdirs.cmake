# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/rohith/Documents/codeProjects/build/_deps/corrosion-src"
  "/home/rohith/Documents/codeProjects/build/_deps/corrosion-build"
  "/mnt/nvme0n1p4/Documents/codeProjects/build/_deps/corrosion-subbuild/corrosion-populate-prefix"
  "/mnt/nvme0n1p4/Documents/codeProjects/build/_deps/corrosion-subbuild/corrosion-populate-prefix/tmp"
  "/mnt/nvme0n1p4/Documents/codeProjects/build/_deps/corrosion-subbuild/corrosion-populate-prefix/src/corrosion-populate-stamp"
  "/mnt/nvme0n1p4/Documents/codeProjects/build/_deps/corrosion-subbuild/corrosion-populate-prefix/src"
  "/mnt/nvme0n1p4/Documents/codeProjects/build/_deps/corrosion-subbuild/corrosion-populate-prefix/src/corrosion-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/mnt/nvme0n1p4/Documents/codeProjects/build/_deps/corrosion-subbuild/corrosion-populate-prefix/src/corrosion-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/mnt/nvme0n1p4/Documents/codeProjects/build/_deps/corrosion-subbuild/corrosion-populate-prefix/src/corrosion-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
