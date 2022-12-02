import { expect } from "chai";
import "mocha";

import { readData } from "../reader";
import { readExample } from "../lib";

describe("Day01", () => {
  describe("when the test input is read", () => {
    it("returns the parsed data", () => {
      const result = readData(readExample());

      expect(result).to.deep.equal([
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
      ]);
    });
  });
});
