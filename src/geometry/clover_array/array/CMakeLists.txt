#    This file is part of nutr.
#
#    nutr is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    nutr is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with nutr.  If not, see <https://www.gnu.org/licenses/>.
#
#    Copyright (C) 2020, 2021 Udo Friman-Gayer

add_library(beamPipe EXCLUDE_FROM_ALL BeamPipe.cc)
target_include_directories(beamPipe PUBLIC ${PROJECT_SOURCE_DIR}/include/geometry/clover_array/array)

add_library(collimatorRoom EXCLUDE_FROM_ALL CollimatorRoom.cc)
target_include_directories(collimatorRoom PUBLIC ${PROJECT_SOURCE_DIR}/include/geometry/clover_array/array)

add_library(comptonMonitor EXCLUDE_FROM_ALL ComptonMonitor.cc)
target_include_directories(comptonMonitor PUBLIC ${PROJECT_SOURCE_DIR}/include/geometry/clover_array/array)

add_library(leadShieldingUTR EXCLUDE_FROM_ALL LeadShieldingUTR.cc)
target_include_directories(leadShieldingUTR PUBLIC ${PROJECT_SOURCE_DIR}/include/geometry/clover_array/array)