import { expect } from "chai";
import "mocha";

import { readData } from "../reader";
import { readExample } from "../lib";
import { Shape } from "../model";

describe("Day02Reader", () => {
  describe("when the test input is read", () => {
    it("returns the parsed data", () => {
      const result = readData(readExample());

      expect(result).to.deep.equal([
        { opponent: Shape.Rock, mine: Shape.Paper },
        { opponent: Shape.Paper, mine: Shape.Rock },
        { opponent: Shape.Scissors, mine: Shape.Scissors },
      ]);
    });
  });
});
