/*
    This file is part of nutr.

    nutr is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    nutr is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with nutr.  If not, see <https://www.gnu.org/licenses/>.

    Copyright (C) 2020 Udo Friman-Gayer
*/

// Based on Geant4 10.6.1 example
//
// ${CMAKE_INSTALL_PREFIX}/share/Geant4/examples/extended/analysis/AnaEx02

#pragma once

#include "g4root.hh"
#include "globals.hh"

#include "DetectorHit.hh"

class TupleManager
{
  public:
    TupleManager();
   ~TupleManager();

    void Book();
    void Save();

    void FillNtuple(G4int deid, G4double edep);

  private:
    G4bool fFactoryOn;
};