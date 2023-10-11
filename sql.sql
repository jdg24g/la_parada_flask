-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bus_schedule
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `bus_schedule` ;

-- -----------------------------------------------------
-- Schema bus_schedule
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bus_schedule` DEFAULT CHARACTER SET utf8 ;
USE `bus_schedule` ;

-- -----------------------------------------------------
-- Table `bus_schedule`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bus_schedule`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bus_schedule`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bus_schedule`.`cities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `city_UNIQUE` (`city` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bus_schedule`.`companies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bus_schedule`.`companies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `company` VARCHAR(255) NULL,
  `phone` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `company_UNIQUE` (`company` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bus_schedule`.`schedules`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bus_schedule`.`schedules` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `company_id` INT NOT NULL,
  `city_id` INT NOT NULL,
  `schedule` TIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_schedule_companies_idx` (`company_id` ASC) VISIBLE,
  INDEX `fk_schedule_cities1_idx` (`city_id` ASC) VISIBLE,
  CONSTRAINT `fk_schedule_companies`
    FOREIGN KEY (`company_id`)
    REFERENCES `bus_schedule`.`companies` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_schedule_cities1`
    FOREIGN KEY (`city_id`)
    REFERENCES `bus_schedule`.`cities` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
