require 'json'

class Account
  attr_accessor :name, :balance

  def initialize(name, balance)
    @name = name
    @balance = balance
  end

  def self.from_json(json_obj)
    name = json_obj.keys.first
    balance = json_obj.dig('extra', 'balance') || json_obj.dig(name, 'balance')
    new(name, balance)
  end

  def self.sort_by_balance(accounts)
    accounts.sort_by(&:balance)
  end

  # Start from the back: for every 3 digits from the back, if there exists a next digit, prepend a comma.
  def formatted_balance
    @balance.to_s.reverse.gsub(/(\d{3})(?=\d)/, '\1,').reverse
  end

  def to_s
    "#{@name}: #{formatted_balance}"
  end
end

def read_and_parse_json
  json_strings = ARGF.readlines
  json_strings.map { |json_str| JSON.parse(json_str) }
              .map { |json_obj| Account.from_json(json_obj) }
end

def main
  accounts = read_and_parse_json
  sorted_accounts = Account.sort_by_balance(accounts)
  sorted_accounts.each { |account| puts account }
end

main if $PROGRAM_NAME == __FILE__
